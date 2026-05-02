from sklearn.preprocessing import LabelEncoder
import pandas as pd 
df = pd.read_csv("PRACTICE/sample_data.csv")

df_label = df.copy()
le = LabelEncoder()
df_label["Gender_Encoded"] = le.fit_transform(df_label["Gender"])
df_label["Passed_Encoded"] = le.fit_transform(df_label["Passed"])
print("\Label Encoded data")
print(df_label[["Name","Gender","Gender_Encoded","Passed","Passed_Encoded"]])


df_encoded = pd.get_dummies(df_label,columns=["City"])
print("\One-Hot Encoded data (City)")
print(df_encoded)
