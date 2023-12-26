from PySide6.QtWidgets import QMessageBox
from file_py.common import select_file
import pandas as pd
from file_py.SqlHelper import SqlHelper
from file_py.sqlite import SQLiteMemory


class FileManager:
    def __init__(self):
        super().__init__()
        self.sqlHelper = SqlHelper()
        self.sqliteMemory = SQLiteMemory()
        # 如果内存数据库为空，则提示用户导入数据
        if self.sqliteMemory.execute_query("SELECT count(*) FROM Item_version") == 0:
            QMessageBox.information(None, "系统消息", "请先导入数据")

    def add(self):
        path = select_file("请选择要添加数据的Excel文件")
        if path:
            df = pd.read_excel(path, sheet_name='Sheet1', usecols=['编码', '当前版本', '历史版本'])
            if df.empty:
                QMessageBox.warning(None, "系统消息", "文件为空")
                return
            else:
                df.rename(columns={'编码': 'Item', '当前版本': 'C_version', '历史版本': 'H_version'}, inplace=True)
                if self.sqlHelper.inster_sqlserver(df=df) > 0:
                    QMessageBox.information(None, "系统消息", "添加成功")
                else:
                    QMessageBox.warning(None, "系统消息", "添加失败")

    def update(self):
        path = select_file("请选择要添加数据的Excel文件")
        if path:
            df = pd.read_excel(path, sheet_name='Sheet2', usecols=['编码', '当前版本', '历史版本'])
            if df.empty:
                QMessageBox.warning(None, "系统消息", "文件为空")
                return
            else:
                df.rename(columns={'编码': 'Item', '当前版本': 'C_version', '历史版本': 'H_version'}, inplace=True)
                if self.sqlHelper.update_sqlserver(df=df) > 0:
                    QMessageBox.information(None, "系统消息", "修改成功")
                else:
                    QMessageBox.warning(None, "系统消息", "修改失败")

    def delete(self):
        path = select_file("请选择要添加数据的Excel文件")
        if path:
            df = pd.read_excel(path, sheet_name='Sheet3', usecols=['编码'])
            if df.empty:
                QMessageBox.warning(None, "系统消息", "文件为空")
                return
            else:
                df.rename(columns={'编码': 'Item'}, inplace=True)
                if self.sqlHelper.Delete_SQLServer(df=df) > 0:
                    QMessageBox.information(None, "系统消息", "删除成功")

    def query(self, item):
        # 查询Item='02350DSD'的内存数据库中的数据
        sql = f"SELECT Item, C_version, H_version FROM Item_version WHERE Item='{item}'"
        # Use pandas to query the in-memory database
        return pd.read_sql_query(sql, self.sqliteMemory.memory_conn)
