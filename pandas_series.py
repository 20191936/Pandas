import pandas as pd

a = pd.Series([1, 2, 3])
print(a)

v = [1,2,3]
x = pd.Series(v,index=['s','d','s'])
print(x)
k_v = {'zhang':1,'shi':2,'jie':3}
y = pd.Series(k_v,index = ['shi','jie'],name = 'name')
print(y)


