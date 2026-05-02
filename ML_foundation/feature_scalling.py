#-----syntax-------------------  
# from sklearn.preprocessing import StandardScaler , MinMaxScaler

# scaler = StandardScaler()
# x_scaled = scaler.fit_transform()

# # Min Max scaler---------

# scaler = MinMaxScaler()
# x_scaled = scaler.fit_transform()


import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data = {
  "study_hours": [1, 2, 3, 4, 5],
  "test_score": [40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

# standard_scaler = StandardScaler()
# standard_scaled = standard_scaler.fit_transform(df)

# print("Standard Scaler Output:")
# print(pd.DataFrame(standard_scaled, columns=["study_hours", "test_score"]))


#MinMaxScaler---------

minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
print("\n MinMax scaled output")
print(pd.DataFrame(minmax_scaled , columns=["study_hours","test_score"]))


# train_test_split

x = df[["study_hours"]]
y = df[["test_score"]]

x_train, x_test, y_tain, y_test = train_test_split(x,y, test_size=0.2,random_state=42)
print("Training Data")
print(x_train)

print("Test Data")
print(x_test)