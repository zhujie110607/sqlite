import sqlite3
import pandas as pd
import pymssql

# 连接SQLite数据库，如果数据库不存在，则创建
def connect_sqlite(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    return conn


# 创建表
def create_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS ItemVision(
        Item VARCHAR(15),
        C_version TEXT,
        H_version TEXT,
        PRIMARY KEY(Item)
    )
    """
    conn.execute(sql)


# 将DataFrame中的数据导入到SQLite数据库
def insert_data(df, conn, sql):
    try:
        old_data = pd.DataFrame()
        unique_items = pd.DataFrame()
        old_data = pd.read_sql(sql, conn)  # 先查询数据库中现有的数据，将查询结果转换为DataFrame
        if len(old_data) > 0:  # 如果数据库中有数据
            unique_items = df[~df.index.isin(old_data.set_index('Item').index)]  # 找出新数据和已有数据的差集
            if len(unique_items) > 0:  # 如果新数据不为空，则将新数据导入到数据库
                unique_items.reset_index(inplace=True)
                unique_items.to_sql('ItemVision', conn, if_exists='append', index=False, method='multi', chunksize=1000)
            else:
                print('No new data')
                return True
        else:
            df.reset_index(inplace=True)
            df.to_sql('ItemVision', conn, if_exists='append', index=False, method='multi', chunksize=1000)
        return True
    except Exception as e:
        print(e)
        return False


def create_memory(conn):
    # 连接到SQLite数据库
    # conn = sqlite3.connect(your_database_file)
    # 创建一个内存数据库
    memory_conn = sqlite3.connect(":memory:")
    # 创建一个游标对象
    cursor = conn.cursor()
    # 创建一个与内存数据库中表结构相同的表
    memory_cursor = memory_conn.cursor()
    # 查询原数据库中的表结构
    cursor.execute("SELECT * FROM ItemVision")
    columns = [column[0] for column in cursor.description]
    # 在内存数据库中创建相同的表
    memory_cursor.execute("CREATE TABLE ItemVision (" + ",".join(["'"+str(column)+"'" for column in columns]) + ")")
    # 查询原数据库中的数据
    cursor.execute("SELECT * FROM ItemVision")
    rows = cursor.fetchall()
    # 将数据插入到内存数据库的表中
    for row in rows:
        memory_cursor.execute("INSERT INTO ItemVision VALUES (?,?,?)", row)
    # 提交内存数据库的更改
    memory_conn.commit()
    # 查询内存数据库的表中的数据
    for row in memory_cursor.execute("SELECT * FROM ItemVision"):
        print(row)
    # 关闭与SQLite数据库的连接
    cursor.close()
    conn.close()
    # 关闭内存数据库的连接
    memory_conn.close()




def Query_SQLServer():
    con= pymssql.connect(
        server='192.168.1.7',
        user='sa',
        password='cj126414.',
        database='AnJiServer'
    )
    # 创建游标
    cursor = con.cursor()

    # 执行SQL查询
    sql = "SELECT Item,ContractNO,Qty FROM PL_Item"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 把查询结果转换为DataFrame
    df = pd.DataFrame(results, columns=['Item', 'ContractNO', 'Qty'])
    # 关闭游标和连接
    cursor.close()
    con.close()
    return df


def create_memory():
    # 创建一个内存数据库
    memory_conn = sqlite3.connect(":memory:")
    # 创建一个与内存数据库中表结构相同的表
    memory_cursor = memory_conn.cursor()
    # 在内存数据库中创建相同的表
    memory_cursor.execute("CREATE TABLE PL_Item (Item varchar(20),ContractNO varchar(15),Qty int)")
    # 查询SQL SERVER数据库中的数据
    df=Query_SQLServer()
    # 将数据插入到内存数据库的表中
    rows = df.values.tolist()
    for row in rows:
        memory_cursor.execute("INSERT INTO PL_Item VALUES (?,?,?)", row)
    # 提交内存数据库的更改
    memory_conn.commit()
    # 查询Item='03026HTW'的内存数据库中的数据
    for row in memory_cursor.execute("SELECT Item,ContractNO,Qty FROM PL_Item WHERE Item='03026HTW'"):
        print(row)
    # 关闭内存数据库的连接
    memory_conn.close()





