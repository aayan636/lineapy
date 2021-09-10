import pytest

import lineapy.app.app_db
from lineapy import ExecutionMode
from tests.util import setup_db


@pytest.fixture(autouse=True)
def test_db_mock(monkeypatch):
    test_db = setup_db(ExecutionMode.TEST, reset=True)
    monkeypatch.setattr(lineapy.app.app_db, "lineadb", test_db)


# NOTE: @Yifan please uncomment this test when you've implemented line and column numbers in transformer
# def test_executor_and_db_apis(test_db_mock):
#     from lineapy.app.app_db import lineadb

#     s = lineadb.data_asset_manager.read_node_value(
#         UUID("ccebc2e9-d710-4943-8bae-947fa1492d7f"), 1
#     )
#     assert s == 25