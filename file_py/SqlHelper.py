import pandas as pd
from PySide6.QtWidgets import QMessageBox
from sqlalchemy import create_engine, delete, MetaData, Column, Table, update
from sqlalchemy.types import String


class SqlHelper:
    def __init__(self):
        self.engine = create_engine('mssql+pyodbc://sa:cj126414.@192.168.0.153/Fr?driver=ODBC+Driver+17+for+SQL+Server',
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
    def inster_sqlserver(self, df):  # df是DataFrame
        # 指定数据类型
        dtype = {'Item': String(20), 'C_version': String(100), 'H_version': String(200)}

        # 开始事务
        with self.engine.begin() as connection:
            try:
                # 将 DataFrame 写入数据库
                df.to_sql('Item_version', con=connection, if_exists="append", index=False, dtype=dtype)
            except Exception as e:
                # 处理插入失败的情况
                connection.rollback()  # 回滚事务，撤销之前的操作
                QMessageBox.critical(None, '错误', f'插入或更新失败：{e}')
                return 0
            else:
                connection.commit()  # 提交事务
                return len(df)

    def update_sqlserver(self, df):
        # 开始事务
        with self.engine.begin() as connection:
            try:
                # 循环处理 DataFrame 中的每一行数据
                for index, row in df.iterrows():
                    update_data = {'C_version': row['C_version'], 'H_version': row['H_version']}
                    # 构建更新条件
                    update_condition = self.Item_version.c.Item == row['Item']

                    # 使用 update 方法构建更新语句
                    update_stmt = update(self.Item_version).values(update_data).where(update_condition)

                    # 使用 execute 方法执行 UPDATE 语句
                    result = connection.execute(update_stmt)
            except Exception as e:
                # 处理更新失败的情况
                connection.rollback()  # 回滚事务，撤销之前的操作
                QMessageBox.critical(None, '错误', f'更新失败：{e}')
                return -1  # Return -1 in case of failure
            else:
                connection.commit()  # 提交事务
                return result.rowcount

    # 删除SQL SERVER数据库
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
                connection.rollback()  # 回滚事务，撤销之前的操作
                QMessageBox.critical(None, '错误', f'删除失败：{e}')
                return 0
            else:
                return deleted_rows

    # 查询SQL SERVER数据库
    def Query_SQLServer_by_SQL(self, sql):
        try:
            df = pd.read_sql_query(sql, self.engine)
            return df
        except Exception as e:
            QMessageBox.critical(None, '错误', f'查询失败：{e}')
            # 返回空的DataFrame
            return pd.DataFrame()
