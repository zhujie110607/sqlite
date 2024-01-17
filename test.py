import pandas as pd

# 假设 df 是你的 DataFrame，其中包含名为 'Item' 的列
df = pd.DataFrame({'Item': ['03053774', '03052363', '03051111']})

# 将 'Item' 列的值转换为字符串，并使用逗号分隔
items_str = ','.join(f"'{item}'" for item in df['Item'])

# 构造 DELETE 语句
delete_query = f"DELETE Item_version WHERE Item IN ({items_str})"

print(delete_query)






