import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import pandas as pd\ndf = pd.DataFrame([1,2])\nassert df.size == 2\n",
    working_directory="dummy_linea_repo/",
    session_name=None,
    user_name=None,
    hardware_spec=None,
    libraries=[
        Library(
            id=get_new_id(),
            name="pandas",
            version=None,
            path=None,
        ),
    ],
)
import_1 = ImportNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=19,
    library=Library(
        id=get_new_id(),
        name="pandas",
        version=None,
        path=None,
    ),
    attributes=None,
    alias="pd",
    module=None,
)
literal_1 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=19,
    end_lineno=2,
    end_col_offset=20,
    value=1,
)
literal_2 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=21,
    end_lineno=2,
    end_col_offset=22,
    value=2,
)
literal_3 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    value="size",
)
literal_4 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=18,
    end_lineno=3,
    end_col_offset=19,
    value=2,
)
argument_1 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=literal_1.id,
    value_literal=None,
)
argument_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=1,
    value_node_id=literal_2.id,
    value_literal=None,
)
argument_3 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=1,
    value_node_id=literal_3.id,
    value_literal=None,
)
argument_4 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=1,
    value_node_id=literal_4.id,
    value_literal=None,
)
call_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=18,
    end_lineno=2,
    end_col_offset=23,
    arguments=[argument_1.id, argument_2.id],
    function_name="__build_list__",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name=None,
    value=None,
)
argument_5 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=call_1.id,
    value_literal=None,
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=24,
    arguments=[argument_5.id],
    function_name="DataFrame",
    function_module=import_1.id,
    locally_defined_function_id=None,
    assigned_variable_name="df",
    value=None,
)
argument_6 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=call_2.id,
    value_literal=None,
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=7,
    end_lineno=3,
    end_col_offset=14,
    arguments=[argument_3.id, argument_6.id],
    function_name="getattr",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name=None,
    value=None,
)
argument_7 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=call_3.id,
    value_literal=None,
)
call_4 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=7,
    end_lineno=3,
    end_col_offset=19,
    arguments=[argument_4.id, argument_7.id],
    function_name="eq",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name=None,
    value=None,
)