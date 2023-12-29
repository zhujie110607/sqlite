import os

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
        if QMessageBox.warning(None, "系统消息", "您点击了添加按钮，请确认是否要添加数据",
                               QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            path = select_file("请选择要添加数据的Excel文件")
            if path:
                df = pd.read_excel(path, sheet_name='添加', usecols=['编码', '当前版本', '历史版本'])
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
        if QMessageBox.warning(None, "系统消息", "您点击了修改按钮，请确认是否要修改数据",
                               QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            path = select_file("请选择要添加数据的Excel文件")
            if path:
                df = pd.read_excel(path, sheet_name='更新', usecols=['编码', '当前版本', '历史版本'])
                if df.empty:
                    QMessageBox.warning(None, "系统消息", "文件为空")
                    return
                else:
                    df.rename(columns={'编码': 'Item', '当前版本': 'C_version', '历史版本': 'H_version'}, inplace=True)
                    if self.sqlHelper.update_sqlserver(df=df) > 0:
                        QMessageBox.information(None, "系统消息", "修改成功")
                    else:
                        QMessageBox.warning(None, "系统消息", "修改失败")

    def match(self):
        dfsqlite = self.query_all()
        if dfsqlite.empty:
            QMessageBox.warning(None, "系统消息", "内存数据库为空")
            return
        # 把Item设置为行索引
        dfsqlite.set_index('Item', inplace=True)

        path = select_file("请选择要匹配数据的Excel文件")
        if path:
            df = pd.read_excel(path, sheet_name='找差异', usecols=['编码', '当前版本', '历史版本'])
        if df.empty:
            QMessageBox.warning(None, "系统消息", "文件为空")
            return
        else:
            df.rename(columns={'编码': 'Item', '当前版本': 'C_version', '历史版本': 'H_version'}, inplace=True)
            df.set_index('Item', inplace=True)
            df_index = df.index.difference(dfsqlite.index)  # 找出df中没有在dfsqlite中出现的行
            # 找出两个DataFrame都有的行索引
            common_index = df.index.intersection(dfsqlite.index)
            # 初始化一个空的DataFrame来存储结果
            result = pd.DataFrame()
            # 遍历每一个共有的行索引
            for index in common_index:
                # 如果df1和df2在该行索引处的数据不同，则将该行添加到结果中
                if not df.loc[index].equals(dfsqlite.loc[index]):
                    result = result._append(
                        pd.concat([df[df.index == index], dfsqlite[dfsqlite.index == index]], axis=1))
            with pd.ExcelWriter('差异.xlsx') as writer:
                if ~df_index.empty:
                    df[df.index.isin(df_index.tolist())].to_excel(writer, sheet_name='数据库中没有的数据', index=True)
                if result.shape[0] > 0:
                    result.to_excel(writer, sheet_name='都有的编码但是数据有差异', index=True)
                # writer._save()
                writer.close()
                QMessageBox.information(None, "系统消息", "导出成功")

    def delete(self):
        if QMessageBox.warning(None, "系统消息", "您点击了删除按钮，请确认是否要删除数据",
                               QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            path = select_file("请选择要添加数据的Excel文件")
            if path:
                df = pd.read_excel(path, sheet_name='删除', usecols=['编码'])
                if df.empty:
                    QMessageBox.warning(None, "系统消息", "文件为空")
                    return
                else:
                    df.rename(columns={'编码': 'Item'}, inplace=True)
                    if self.sqlHelper.Delete_SQLServer(df=df) > 0:
                        QMessageBox.information(None, "系统消息", "删除成功")

    # 导出数据
    def export(self):
        # 询问用户是否导出数据，如果是，则导出数据
        if QMessageBox.question(None, "系统消息", "是否导出数据", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            df = self.query_all()
            if df.empty:
                QMessageBox.warning(None, "系统消息", "查询结果为空")
            else:
                # 导出数据
                df.to_excel('data.xlsx', index=False)
                # 打开文件导出的文件
                os.startfile('data.xlsx')

    def query_all(self):
        sql = "SELECT Item, C_version, H_version FROM Item_version"
        return pd.read_sql_query(sql, self.sqliteMemory.memory_conn)

    def query(self, item):
        # 查询Item='02350DSD'的内存数据库中的数据
        sql = f"SELECT Item, C_version, H_version FROM Item_version WHERE Item='{item}'"
        # Use pandas to query the in-memory database
        return pd.read_sql_query(sql, self.sqliteMemory.memory_conn)
