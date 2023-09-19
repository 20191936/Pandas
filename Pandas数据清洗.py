import pandas as pd

#1 pandas 清洗空值
df  = pd.read_csv('./property-data.csv')
print(df.head())

print(df['NUM_BEDROOMS'])
# isnull 判断是否为空
print(df['NUM_BEDROOMS'].isnull())
# 只会删除空行
new_df = df.dropna()
print(new_df.to_string())

# 使用inplace 修改源数据
df.dropna(inplace=True,subset=['ST_NUM'])
print(df.to_string())

# miss_values = ['n/a','na','--']
# df = pd.read_csv('property-data.csv',na_values = miss_values)
#
# print(df['NUM_BEDROOMS'])
# # isnull 判断是否为空
# print(df['NUM_BEDROOMS'].isnull())

# filena 替换空数据
df = pd.read_csv('property-data.csv')

df['PID'].fillna(12345, inplace = True)

print(df.to_string())
x = df['ST_NUM'].mean()
print(df['ST_NUM'].mean())
print(df['ST_NUM'].sum())
# 用平均自替换确实元素
df['ST_NUM'].fillna(x,inplace=True)
print(df)

# 用众数替换缺失元素
x = df['ST_NUM'].mode()
df['ST_NUM'].fillna(x,inplace=True)
print(df.to_string())

#数据格式错误的单元格会使数据分析变得困难，甚至不可能。我们可以通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据。
data = {
  "Date": ['2020/12/01', '2020/12/02' , '2020/12/26'],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# 去重
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)

df = df.drop_duplicates()
print(df.to_string())
