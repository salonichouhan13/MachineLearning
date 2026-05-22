import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# data sample
data = {
  "Cluster" : ["riya","aman","neha","sneha","rashi","shruti"],
  "Age": [20,30,28,42,25,38],
  "Spending" :[100,200,300,110,290,130]
}
df = pd.DataFrame(data)
print(df)

X = df[["Age","Spending"]]

#call kmeans
model = KMeans(n_clusters=2,random_state=42,n_init=10)

df["Group"] = model.fit_predict(X)

plt.figure(figsize=(6,5))
for group in df["Group"].unique():
  group_data = df[df["Group"]==group]
  plt.scatter(group_data["Age"],group_data["Spending"], label= f"Group{group}")

plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Customer Sagement (K_Means)")
plt.legend()
plt.grid(True)
plt.show()
