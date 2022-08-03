"""CSVMS SQL Engine Module
See https://github.com/Didone/csvms/discussions/6
"""
from mo_sql_parsing import parse
from csvms.table import Table

class Engine():
    """Class used to implement bootcamp tasks"""

    def execute(self, sql:str):
        """Execute SQL statement
        :param sql: String with sql statement"""
        ast = parse(sql)
        if ast.get('create table') is not None:
            self._create_table(
                name = ast['create table']['name'],
                columns = ast['create table']['columns']
            )
        elif ast.get('drop') is not None:
                self._drop_table(
                    name = ast['drop']['table']
                )

    def _create_table(self, name: str, columns: list):
        print()

    def _drop_table(self, name: str):
        print()