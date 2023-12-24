import pandas as pd
import common

# with common.connect_sqlite('demo.db') as conn:  # 创建或连接数据库
#     common.create_table(conn)  # 创建表
#     df = pd.read_excel('item.xlsx',index_col='Item')  # 获取数据
#     # 插入数据到表read_csv
#     sql = 'SELECT Item FROM ItemVision'  # 查询数据库已有的数据
#     bo=common.insert_data(df, conn, sql)
#     if bo:
#         print('插入成功')
#         common.create_memory(common.connect_sqlite('demo.db'))
#     else:
#         print('插入失败')

common.create_memory()
print('查询成功')

