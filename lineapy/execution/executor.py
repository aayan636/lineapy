import builtins
import importlib.util
import io
import subprocess
import sys
from typing import Any

from lineapy.data.graph import Graph
from lineapy.data.types import SessionContext, NodeType
from lineapy.db.asset_manager.base import DataAssetManager
from lineapy.graph_reader.base import GraphReader


class Executor(GraphReader):

    def __init__(self):
        self._variable_values = {}

        # Note: no output will be shown in Terminal because it is being redirected here
        self._old_stdout = sys.stdout
        self._stdout = io.StringIO()

    @property
    def data_asset_manager(self) -> DataAssetManager:
        pass

    def setup(self, context: SessionContext) -> None:
        """
        TODO set up the execution environment based on `context`
        """
        pass

    def get_stdout(self) -> str:
        """
        This returns the text that corresponds to the stdout results.
        For instance, `print("hi")` should yield a result of "hi\n" from this function.

        Note:
        - If we assume that everything is sliced, the user printing may not happen, but third party libs may still have outputs.
        - Also the user may manually annotate for the print line to be included and in general stdouts are useful
        """

        val = self._stdout.getvalue()
        return val

    def get_value_by_variable_name(self, name: str) -> Any:
        return self._variable_values[name]

    def walk(self, program: Graph) -> None:

        sys.stdout = self._stdout

        def install(package):
            subprocess.check_call([sys.executable, "-m", 'pip', 'install', package])

        def lookup_module(call_node):
            if call_node.function_module is None:
                return builtins

            import_node = program.get_node(call_node.function_module)
            if import_node.module is None:
                import_node.module = importlib.import_module(import_node.library.name)

            return import_node.module

        def setup_context_for_node(node, scoped_locals):
            for state_var in node.state_change_nodes:
                state_var = program.get_node(state_var)
                initial_state = program.get_node(state_var.initial_value_node_id)
                if initial_state.node_type in [NodeType.CallNode, NodeType.LiteralAssignNode, NodeType.StateChangeNode]:
                    initial_state = initial_state.value
                    scoped_locals[state_var.variable_name] = initial_state
            
            # TODO: handling use of modules within loops
            if node.import_nodes:
                for import_node in node.import_nodes:
                    import_node = program.get_node(import_node)
                    if importlib.util.find_spec(import_node.library.name) is None:
                        install(import_node.library.name)
                    import_node.module = importlib.import_module(import_node.library.name)
                    scoped_locals[import_node.library.name] = import_node.module


        def update_node_side_effects(node, scoped_locals):
            local_vars = scoped_locals
            for state_var in node.state_change_nodes:
                state_var = program.get_node(state_var)

                state_var.value = local_vars[state_var.variable_name]

                if state_var.variable_name:
                    self._variable_values[state_var.variable_name] = state_var.value

        for node_id in program.visit_order():
            node = program.get_node(node_id)
            scoped_locals = locals()

            # all of these have to be in the same scope in order to read 
            # and write to scoped_locals properly (this is just the way exec works)

            if node.node_type == NodeType.CallNode:
                fn_name = node.function_name
                fn = None

                if node.locally_defined_function_id:
                    fn = scoped_locals[fn_name]
                else:
                    if node.function_module and program.get_node(node.function_module).attributes:
                        fn_name = program.get_node(node.function_module).attributes[node.function_name]
                    
                    fn = getattr(lookup_module(node), fn_name)

                args = []
                for arg in node.arguments:
                    if arg.value_literal:
                        args.append(arg.value_literal)
                    elif arg.value_node_id:
                        args.append(program.get_node(arg.value_node_id).value)

                val = fn(*args)

                if val is not None:
                    node.value = val

                if node.assigned_variable_name:
                    self._variable_values[node.assigned_variable_name] = node.value
                
                if node.locally_defined_function_id:
                    update_node_side_effects(program.get_node(node.locally_defined_function_id), scoped_locals)

            elif node.node_type == NodeType.ImportNode:
                if importlib.util.find_spec(node.library.name) is None:
                    install(node.library.name)
                node.module = importlib.import_module(node.library.name)

            elif node.node_type == NodeType.LoopNode:
                # set up vars and imports
                setup_context_for_node(node, scoped_locals)
                exec(node.code)
                update_node_side_effects(node, scoped_locals)
                
            elif node.node_type == NodeType.FunctionDefinitionNode:
                setup_context_for_node(node, scoped_locals)
                exec(node.code, scoped_locals)

        sys.stdout = self._old_stdout

    def validate(self, program: Graph) -> None:
        pass
