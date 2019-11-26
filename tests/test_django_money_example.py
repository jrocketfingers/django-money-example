import pytest
from django.db import connections
from django.db.migrations.executor import MigrationExecutor

from django_money_example.core import models


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.django_db
def test_sql_migrations():
    connection = connections["default"]
    executor = MigrationExecutor(connection)

    migration = executor.loader.get_migration_by_prefix("core", "0002")
    targets = [("core", migration.name)]
    plan = [(executor.loader.graph.nodes[targets[0]], False)]

    import pdb; pdb.set_trace()
    sql_statements = executor.collect_sql(plan)
