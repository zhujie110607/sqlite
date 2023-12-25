import pandas as pd
import pymssql
from PySide6.QtWidgets import QMessageBox


class SqlHelper:
    def Query_SQLServer(sql):
        try:
            con = pymssql.connect(
                server='192.168.0.153',
                user='sa',
                password='cj126414.',
                database='Fr',
                charset='GBK'  # 编码格式 中文简体
            )
            # 创建游标
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            fields = [field[0] for field in cursor.description]
            # 把查询结果转换为DataFrame
            return pd.DataFrame(results, columns=fields)
        except Exception as e:
            QMessageBox.critical(None, '错误', f'查询失败：{e}')
            # 返回空的DataFrame
            return pd.DataFrame()
        finally:
            if con:
                con.close()
            if cursor:
                cursor.close()
