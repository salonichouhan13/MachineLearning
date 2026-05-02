import pandas as pd 
data = {
  "name" :["kanha","sargun","saloni","kajal","vinisha"],
  "age" : [18,16,20,None ,None],
  "salary" : [40000,50000,140000,None,None ]
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