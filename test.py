import pandas as pd
# from file_py.SqlHelper import SqlHelper

# sql='select Item,C_version,H_version from Item_version'
# sql="select UserNumber,UserName,UserPwd,privs from UserManagement"
# df=pd.read_excel('item.xlsx',sheet_name='Sheet2')
#
#
#
# i=SqlHelper().Delete_SQLServer(df)
# print(i)
df=pd.DataFrame({'name':['zhujie1','wu'],'age':[18,20]})
print(19==df[df['name']=='zhujie1']['age'].values)





