import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    working_directory="dummy_linea_repo/",
    libraries=[],
)
source_1 = SourceCode(
    id=get_new_id(),
    code="""from pandas import DataFrame
df = DataFrame([[1,2], [3,4]])
df[0].astype(str)
assert df.size == 4
new_df = df.iloc[:, 1]
assert new_df.size == 2
""",
    location=PosixPath(
        "[source file path]"
    ),
)
variable_2 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=2,
        col_offset=0,
        end_lineno=2,
        end_col_offset=30,
        source_code=source_1.id,
    ),
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=2,
            col_offset=5,
            end_lineno=2,
            end_col_offset=30,
            source_code=source_1.id,
        ),
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    source_location=SourceLocation(
                        lineno=2,
                        col_offset=15,
                        end_lineno=2,
                        end_col_offset=29,
                        source_code=source_1.id,
                    ),
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=CallNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=2,
                                    col_offset=16,
                                    end_lineno=2,
                                    end_col_offset=21,
                                    source_code=source_1.id,
                                ),
                                arguments=[
                                    ArgumentNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        positional_order=0,
                                        value_node_id=LiteralNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            source_location=SourceLocation(
                                                lineno=2,
                                                col_offset=17,
                                                end_lineno=2,
                                                end_col_offset=18,
                                                source_code=source_1.id,
                                            ),
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
                                            source_location=SourceLocation(
                                                lineno=2,
                                                col_offset=19,
                                                end_lineno=2,
                                                end_col_offset=20,
                                                source_code=source_1.id,
                                            ),
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
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=CallNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=2,
                                    col_offset=23,
                                    end_lineno=2,
                                    end_col_offset=28,
                                    source_code=source_1.id,
                                ),
                                arguments=[
                                    ArgumentNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        positional_order=0,
                                        value_node_id=LiteralNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            source_location=SourceLocation(
                                                lineno=2,
                                                col_offset=24,
                                                end_lineno=2,
                                                end_col_offset=25,
                                                source_code=source_1.id,
                                            ),
                                            value=3,
                                        ).id,
                                    ).id,
                                    ArgumentNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        positional_order=1,
                                        value_node_id=LiteralNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            source_location=SourceLocation(
                                                lineno=2,
                                                col_offset=26,
                                                end_lineno=2,
                                                end_col_offset=27,
                                                source_code=source_1.id,
                                            ),
                                            value=4,
                                        ).id,
                                    ).id,
                                ],
                                function_id=LookupNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    name="__build_list__",
                                ).id,
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
        function_id=VariableNode(
            id=get_new_id(),
            session_id=session.id,
            source_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=ImportNode(
                            id=get_new_id(),
                            session_id=session.id,
                            source_location=SourceLocation(
                                lineno=1,
                                col_offset=0,
                                end_lineno=1,
                                end_col_offset=28,
                                source_code=source_1.id,
                            ),
                            library=Library(
                                id=get_new_id(),
                                name="pandas",
                            ),
                            attributes={"DataFrame": "DataFrame"},
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
            assigned_variable_name="DataFrame",
        ).id,
    ).id,
    assigned_variable_name="df",
)
call_8 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=17,
        source_code=source_1.id,
    ),
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
        source_location=SourceLocation(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=12,
            source_code=source_1.id,
        ),
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    source_location=SourceLocation(
                        lineno=3,
                        col_offset=0,
                        end_lineno=3,
                        end_col_offset=5,
                        source_code=source_1.id,
                    ),
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=variable_2.id,
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=3,
                                    col_offset=3,
                                    end_lineno=3,
                                    end_col_offset=4,
                                    source_code=source_1.id,
                                ),
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
call_11 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=4,
        col_offset=0,
        end_lineno=4,
        end_col_offset=19,
        source_code=source_1.id,
    ),
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                source_location=SourceLocation(
                    lineno=4,
                    col_offset=7,
                    end_lineno=4,
                    end_col_offset=19,
                    source_code=source_1.id,
                ),
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=CallNode(
                            id=get_new_id(),
                            session_id=session.id,
                            source_location=SourceLocation(
                                lineno=4,
                                col_offset=7,
                                end_lineno=4,
                                end_col_offset=14,
                                source_code=source_1.id,
                            ),
                            arguments=[
                                ArgumentNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    positional_order=0,
                                    value_node_id=variable_2.id,
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
                            source_location=SourceLocation(
                                lineno=4,
                                col_offset=18,
                                end_lineno=4,
                                end_col_offset=19,
                                source_code=source_1.id,
                            ),
                            value=4,
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
call_18 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=6,
        col_offset=0,
        end_lineno=6,
        end_col_offset=23,
        source_code=source_1.id,
    ),
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                source_location=SourceLocation(
                    lineno=6,
                    col_offset=7,
                    end_lineno=6,
                    end_col_offset=23,
                    source_code=source_1.id,
                ),
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=CallNode(
                            id=get_new_id(),
                            session_id=session.id,
                            source_location=SourceLocation(
                                lineno=6,
                                col_offset=7,
                                end_lineno=6,
                                end_col_offset=18,
                                source_code=source_1.id,
                            ),
                            arguments=[
                                ArgumentNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    positional_order=0,
                                    value_node_id=VariableNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        source_location=SourceLocation(
                                            lineno=5,
                                            col_offset=0,
                                            end_lineno=5,
                                            end_col_offset=22,
                                            source_code=source_1.id,
                                        ),
                                        source_node_id=CallNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            source_location=SourceLocation(
                                                lineno=5,
                                                col_offset=9,
                                                end_lineno=5,
                                                end_col_offset=22,
                                                source_code=source_1.id,
                                            ),
                                            arguments=[
                                                ArgumentNode(
                                                    id=get_new_id(),
                                                    session_id=session.id,
                                                    positional_order=0,
                                                    value_node_id=CallNode(
                                                        id=get_new_id(),
                                                        session_id=session.id,
                                                        source_location=SourceLocation(
                                                            lineno=5,
                                                            col_offset=9,
                                                            end_lineno=5,
                                                            end_col_offset=16,
                                                            source_code=source_1.id,
                                                        ),
                                                        arguments=[
                                                            ArgumentNode(
                                                                id=get_new_id(),
                                                                session_id=session.id,
                                                                positional_order=0,
                                                                value_node_id=variable_2.id,
                                                            ).id,
                                                            ArgumentNode(
                                                                id=get_new_id(),
                                                                session_id=session.id,
                                                                positional_order=1,
                                                                value_node_id=LiteralNode(
                                                                    id=get_new_id(),
                                                                    session_id=session.id,
                                                                    value="iloc",
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
                                                    value_node_id=CallNode(
                                                        id=get_new_id(),
                                                        session_id=session.id,
                                                        source_location=SourceLocation(
                                                            lineno=5,
                                                            col_offset=17,
                                                            end_lineno=5,
                                                            end_col_offset=21,
                                                            source_code=source_1.id,
                                                        ),
                                                        arguments=[
                                                            ArgumentNode(
                                                                id=get_new_id(),
                                                                session_id=session.id,
                                                                positional_order=0,
                                                                value_node_id=CallNode(
                                                                    id=get_new_id(),
                                                                    session_id=session.id,
                                                                    source_location=SourceLocation(
                                                                        lineno=5,
                                                                        col_offset=17,
                                                                        end_lineno=5,
                                                                        end_col_offset=18,
                                                                        source_code=source_1.id,
                                                                    ),
                                                                    arguments=[
                                                                        ArgumentNode(
                                                                            id=get_new_id(),
                                                                            session_id=session.id,
                                                                            positional_order=0,
                                                                            value_node_id=LiteralNode(
                                                                                id=get_new_id(),
                                                                                session_id=session.id,
                                                                            ).id,
                                                                        ).id
                                                                    ],
                                                                    function_id=LookupNode(
                                                                        id=get_new_id(),
                                                                        session_id=session.id,
                                                                        name="slice",
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
                                                                    source_location=SourceLocation(
                                                                        lineno=5,
                                                                        col_offset=20,
                                                                        end_lineno=5,
                                                                        end_col_offset=21,
                                                                        source_code=source_1.id,
                                                                    ),
                                                                    value=1,
                                                                ).id,
                                                            ).id,
                                                        ],
                                                        function_id=LookupNode(
                                                            id=get_new_id(),
                                                            session_id=session.id,
                                                            name="__build_tuple__",
                                                        ).id,
                                                    ).id,
                                                ).id,
                                            ],
                                            function_id=LookupNode(
                                                id=get_new_id(),
                                                session_id=session.id,
                                                name="getitem",
                                            ).id,
                                        ).id,
                                        assigned_variable_name="new_df",
                                    ).id,
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
                            source_location=SourceLocation(
                                lineno=6,
                                col_offset=22,
                                end_lineno=6,
                                end_col_offset=23,
                                source_code=source_1.id,
                            ),
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
