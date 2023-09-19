import pandas as pd

df = pd.read_csv('nba.csv')
print(df.to_string())

print(df)

data = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
df = pd.DataFrame(data)
df.to_csv('site_csv')

print(df.info)