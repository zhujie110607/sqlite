import sqlite3
import sys
import pandas as pd
from PySide6.QtWidgets import QMessageBox

from file_py.SqlHelper import SqlHelper


class SQLiteMemory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLiteMemory, cls).__new__(cls)
            cls._instance._initialize_memory_database()
        return cls._instance

    def _initialize_memory_database(self):
        # 创建一个内存数据库
        self.memory_conn = sqlite3.connect(":memory:")
        # 创建一个与内存数据库中表结构相同的表
        self.memory_cursor = self.memory_conn.cursor()
        # 在内存数据库中创建相同的表
        self.memory_cursor.execute(
            "CREATE TABLE Item_version (Item varchar(20) PRIMARY KEY, C_version varchar(100), H_version varchar(200))")
        # 查询 SQL SERVER 数据库中的数据
        df = SqlHelper().Query_SQLServer_by_SQL('SELECT Item, C_version, H_version FROM Item_version')
        # 将新数据插入到内存数据库的表中
        df.to_sql('Item_version', con=self.memory_conn, if_exists='replace', index=False)

        # 提交内存数据库的更改
        self.memory_conn.commit()

    def execute_query(self, query):
        # Use the connection's execute method to execute the query
        cursor = self.memory_conn.cursor()
        cursor.execute(query)

        # Fetch all rows and return them
        rows = cursor.fetchall()
        return rows
    def close_memory_database(self):
        self.memory_conn.close()

# Example of how to use the SQLiteMemory instance:
# sqlite_memory = SQLiteMemory()
# ... use sqlite_memory in other parts of your code ...

# Note: The SQLiteMemory instance should be created once and then reused throughout your project.
