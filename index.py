import sqlite3
import xlwings as xw
from os import listdir
import pandas as pd
conn = sqlite3.connect('test.db')
# 查询所有数据
cursor=conn.cursor()
df=cursor.execute('select * from studen')
for row in df:
    print(row)
# conn.commit()
conn.close()
# 针对每个excel文件的生成器
def eachXlsx(xlsxFn): # xlsxFn是excel文件路径
    wb=xw.Book(xlsxFn)
    sht=wb.sheets[0]
    for index,row in enumerate(sht.rows):
        if index==0: # 跳过标题
            continue
        # 把row行中的每一个单元格的值提取出来，然后将这些值组成一个元组返回，yield 关键字表示这是一个生成器表达式，它会在每次调用时返回一个新的元组，直到没有更多的元素可以生成
        yield tuple(map(lambda x:x.value,row))

# 从Excel文件中导入数据到SQLite数据库
def Excel_to_sqlite(filename):
    xlsxs=('ExcelFiles\\'+fn for fn in listdir('ExcelFiles')) # 获取ExcelFiles文件中所有文件
    with  sqlite3.connect('test.db') as conn: # 连接数据库
        cur=conn.cursor() # 获取游标
        for xlsx in xlsxs:
            sql='INSERT INTO demo VALUES (?,?,?)' # 批量导入数据
            cur.execute(sql,eachXlsx(xlsx)) # 遍历每个xlsx文件，将其中的数据导入到数据库
            conn.commit()

# 将DataFrame中的数据导入到SQLite数据库
def insert_data(df,sqlite_file,sql):
    with connect_sqlite(sqlite_file) as conn:
        old_data=pd.read_sql(sql,conn) # 先查询数据库中现有的数据，将查询结果转换为DataFrame
        unique_items=df[~df.set_index('Item').index.isin(old_data.set_index('Item').index)] # 找出新数据和已有数据的差集
        unique_items.to_sql('demo',conn,if_exists='append',index=False,method='multi',chunksize=1000)
        conn.commit()

 # 连接SQLite数据库，如果数据库不存在，则创建
def connect_sqlite(sqlite_file):
    conn=sqlite3.connect(sqlite_file)
    return conn