

# 使用列表创建
import pandas as pd

data = [['Google',10],['Runoob',12],['Wiki',13]]

df = pd.DataFrame(data,columns=['Site','Age'])

print(df)

#使用ndarrays创建
data ={'Site':['Google','Runoob','Wiki'],'Age':['10','12','13']}
print(pd.DataFrame(data,index = ('day1','day2','day3')))

# 使用字典创建
data = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
print(pd.DataFrame(data))
print(df.loc[[0,1]])