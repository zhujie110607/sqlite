import pandas as pd
from file_py.SqlHelper import SqlHelper

# sql='select Item,C_version,H_version from Item_version'
# sql="select UserNumber,UserName,UserPwd,privs from UserManagement"
df=pd.read_excel('item.xlsx',sheet_name='Sheet2')



i=SqlHelper().Delete_SQLServer(df)
print(i)






