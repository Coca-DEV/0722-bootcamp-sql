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
        if ast.get ('create table') is not None:
            return self._create_table(
                tbl_name = ast['create table']['name'],
                tbl_columns = ast['create table']['columns']
            )
        elif ast.get ('insert into') is not None:
            return self._insert_table(
                tbl_name = ast['insert'],
                tbl_data = ast['query']['select']
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
        return f"A tabela {tbl_name} foi criada com sucesso!"

    def _insert_table(self, tbl_name: str, tbl_data: list):
        data = tuple()
        tbl = Table(tbl_name)
        for _c_ in tbl_data:
            cvalue = _c_['value']
        tbl.append(tbl_data)

    def _update_table(self):
        print()

    def _delete_item(self):
        print()

    def _insert_num_table(self):
        print()