import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import pandas as pd\ndf = pd.DataFrame([1,2])\ndf[0].astype(str)\nassert df.size == 2\n",
    working_directory="dummy_linea_repo/",
    libraries=[
        Library(
            id=get_new_id(),
            name="pandas",
        ),
    ],
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=2,
        col_offset=0,
        end_lineno=2,
        end_col_offset=24,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=2,
                    col_offset=18,
                    end_lineno=2,
                    end_col_offset=23,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=2,
                                col_offset=19,
                                end_lineno=2,
                                end_col_offset=20,
                                value=1,
                            ).id,
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=2,
                                col_offset=21,
                                end_lineno=2,
                                end_col_offset=22,
                                value=2,
                            ).id,
                        ).id,
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="__build_list__",
                    ).id,
                ).id,
            ).id
        ],
        function_id=CallNode(
            id=get_new_id(),
            session_id=session.id,
            lineno=2,
            col_offset=5,
            end_lineno=2,
            end_col_offset=17,
            arguments=[
                ArgumentNode(
                    id=get_new_id(),
                    session_id=session.id,
                    positional_order=0,
                    value_node_id=ImportNode(
                        id=get_new_id(),
                        session_id=session.id,
                        lineno=1,
                        col_offset=0,
                        end_lineno=1,
                        end_col_offset=19,
                        library=Library(
                            id=get_new_id(),
                            name="pandas",
                        ),
                        alias="pd",
                    ).id,
                ).id,
                ArgumentNode(
                    id=get_new_id(),
                    session_id=session.id,
                    positional_order=1,
                    value_node_id=LiteralNode(
                        id=get_new_id(),
                        session_id=session.id,
                        value="DataFrame",
                    ).id,
                ).id,
            ],
            function_id=LookupNode(
                id=get_new_id(),
                session_id=session.id,
                name="getattr",
            ).id,
        ).id,
    ).id,
    assigned_variable_name="df",
)
call_6 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=17,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=LookupNode(
                id=get_new_id(),
                session_id=session.id,
                name="str",
            ).id,
        ).id
    ],
    function_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=12,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=3,
                    col_offset=0,
                    end_lineno=3,
                    end_col_offset=5,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=variable_1.id,
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=3,
                                col_offset=3,
                                end_lineno=3,
                                end_col_offset=4,
                                value=0,
                            ).id,
                        ).id,
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="getitem",
                    ).id,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    value="astype",
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="getattr",
        ).id,
    ).id,
)
call_9 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=4,
    col_offset=0,
    end_lineno=4,
    end_col_offset=19,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=4,
                col_offset=7,
                end_lineno=4,
                end_col_offset=19,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=CallNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=4,
                            col_offset=7,
                            end_lineno=4,
                            end_col_offset=14,
                            arguments=[
                                ArgumentNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    positional_order=0,
                                    value_node_id=variable_1.id,
                                ).id,
                                ArgumentNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    positional_order=1,
                                    value_node_id=LiteralNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        value="size",
                                    ).id,
                                ).id,
                            ],
                            function_id=LookupNode(
                                id=get_new_id(),
                                session_id=session.id,
                                name="getattr",
                            ).id,
                        ).id,
                    ).id,
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=1,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=4,
                            col_offset=18,
                            end_lineno=4,
                            end_col_offset=19,
                            value=2,
                        ).id,
                    ).id,
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="eq",
                ).id,
            ).id,
        ).id
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="__assert__",
    ).id,
)
