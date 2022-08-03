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
        else:
            raise NotImplementedError

    def _create_table(self, tbl_name: str, tbl_columns: list):
        cols = dict()
        for _c_ in tbl_columns:
            cname = _c_['name']
            ctype = Table.dtypes[list(_c_['type'].keys())[0]]
            cols[cname] = ctype

        Table(name = tbl_name, columns = cols).save()

    def _insert_table(self):
        print()

    def _update_table(self):
        print()

    def _delete_item(self):
        print()

    def _insert_num_table(self):
        print()