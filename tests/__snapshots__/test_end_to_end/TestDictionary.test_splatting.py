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
    code="x = {1: 2, 2:2, **{1: 3, 2: 3}, 1: 4}",
    location=PosixPath(
        "[source file path]"
    ),
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=37,
        source_code=source_1.id,
    ),
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=1,
            col_offset=4,
            end_lineno=1,
            end_col_offset=37,
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
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=5,
                                    end_lineno=1,
                                    end_col_offset=6,
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
                                    lineno=1,
                                    col_offset=8,
                                    end_lineno=1,
                                    end_col_offset=9,
                                    source_code=source_1.id,
                                ),
                                value=2,
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
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=11,
                                    end_lineno=1,
                                    end_col_offset=12,
                                    source_code=source_1.id,
                                ),
                                value=2,
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
                                    lineno=1,
                                    col_offset=13,
                                    end_lineno=1,
                                    end_col_offset=14,
                                    source_code=source_1.id,
                                ),
                                value=2,
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
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=2,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=CallNode(
                                id=get_new_id(),
                                session_id=session.id,
                                arguments=[],
                                function_id=LookupNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    name="__build_dict_kwargs_sentinel__",
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
                                    lineno=1,
                                    col_offset=18,
                                    end_lineno=1,
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
                                            arguments=[
                                                ArgumentNode(
                                                    id=get_new_id(),
                                                    session_id=session.id,
                                                    positional_order=0,
                                                    value_node_id=LiteralNode(
                                                        id=get_new_id(),
                                                        session_id=session.id,
                                                        source_location=SourceLocation(
                                                            lineno=1,
                                                            col_offset=19,
                                                            end_lineno=1,
                                                            end_col_offset=20,
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
                                                            lineno=1,
                                                            col_offset=22,
                                                            end_lineno=1,
                                                            end_col_offset=23,
                                                            source_code=source_1.id,
                                                        ),
                                                        value=3,
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
                                    ArgumentNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        positional_order=1,
                                        value_node_id=CallNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            arguments=[
                                                ArgumentNode(
                                                    id=get_new_id(),
                                                    session_id=session.id,
                                                    positional_order=0,
                                                    value_node_id=LiteralNode(
                                                        id=get_new_id(),
                                                        session_id=session.id,
                                                        source_location=SourceLocation(
                                                            lineno=1,
                                                            col_offset=25,
                                                            end_lineno=1,
                                                            end_col_offset=26,
                                                            source_code=source_1.id,
                                                        ),
                                                        value=2,
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
                                                            lineno=1,
                                                            col_offset=28,
                                                            end_lineno=1,
                                                            end_col_offset=29,
                                                            source_code=source_1.id,
                                                        ),
                                                        value=3,
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
                                    name="__build_dict__",
                                ).id,
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
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=3,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=32,
                                    end_lineno=1,
                                    end_col_offset=33,
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
                                    lineno=1,
                                    col_offset=35,
                                    end_lineno=1,
                                    end_col_offset=36,
                                    source_code=source_1.id,
                                ),
                                value=4,
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
            name="__build_dict__",
        ).id,
    ).id,
    assigned_variable_name="x",
)
