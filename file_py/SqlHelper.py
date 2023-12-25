import pandas as pd
from PySide6.QtWidgets import QMessageBox
from sqlalchemy import create_engine, delete, MetaData, Column, Table
from sqlalchemy.types import String


class SqlHelper:
    def __init__(self):
        self.engine = create_engine('mssql+pyodbc://sa:cj126414.@192.168.1.7/Fr?driver=ODBC+Driver+17+for+SQL+Server',
                                    fast_executemany=True)
        # Define the metadata and the table structure
        self.metadata = MetaData()
        self.Item_version = Table('Item_version', self.metadata,
                                  Column('Item', String, primary_key=True),
                                  # Add other columns as needed
                                  Column('C_version', String),
                                  Column('H_version', String))

        # Create the table if it doesn't exist
        self.metadata.create_all(self.engine)

    # 将DataFrame中的数据导入或更新到SQL SERVER数据库
    def df2sqlserver(self, df, table_name, ifexists):
        # 指定数据类型
        dtype = {'Item': String(20), 'C_version': String(100), 'H_version': String(200)}

        # 开始事务
        with self.engine.begin() as connection:
            try:
                # 将 DataFrame 写入数据库
                result_proxy = df.to_sql(table_name, con=connection, if_exists=ifexists, index=False, dtype=dtype)
                row_count = result_proxy.rowcount if result_proxy is not None else 0
            except Exception as e:
                # 处理插入失败的情况
                print(f"Insert failed: {e}")
                print(f"Error details: {str(e)}")  # Add this line to print detailed error information
                connection.rollback()  # 回滚事务，撤销之前的操作
                return 0
            else:
                connection.commit()  # 提交事务
                return row_count

    def Delete_SQLServer(self, df):
        # 开始事务
        with self.engine.begin() as connection:
            try:
                # 构建删除条件
                delete_condition = df['Item'].astype(str).tolist()

                # 使用 delete 方法构建删除语句
                delete_stmt = delete(self.Item_version).where(self.Item_version.c.Item.in_(delete_condition))

                # 使用 execute 方法执行 DELETE 语句
                result = connection.execute(delete_stmt)

                # 获取删除的行数
                deleted_rows = result.rowcount
            except Exception as e:
                # 处理删除失败的情况
                print(f"Delete failed: {e}")
                connection.rollback()  # 回滚事务，撤销之前的操作
            else:
                return deleted_rows

    def Query_SQLServer_by_SQL(self, sql):
        try:
            df = pd.read_sql_query(sql, self.engine)
            return df
        except Exception as e:
            QMessageBox.critical(None, '错误', f'查询失败：{e}')
            # 返回空的DataFrame
            return pd.DataFrame()
