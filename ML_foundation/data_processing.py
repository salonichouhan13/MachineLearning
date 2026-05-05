import pandas as pd 
data = {
  "name" :["kanha","sargun","kajal","vinisha"],
  "age" : [18,16,23 ,None],
  "salary" : [10000,20000,30000,None ]
}
df = pd.DataFrame(data)
print("original dataframe")
print(df)

print(df.isnull().sum())
df_drop = df.dropna()
print(df_drop)

df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)
print(df)


#----how to calc how many percent data is missing----

print(df.isnull().mean()*100)