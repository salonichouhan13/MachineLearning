import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

# LOAD DATASET

data = pd.read_csv("PROJECTS/DataSet.csv")

X = data[["Hours"]] # 2d input
Y = data["Score"] #target column

model = LinearRegression()
model.fit(X,Y)
predict_score = model.predict(X)
 
  
#evaluate
MAE = mean_absolute_error(Y,predict_score)
MSE = mean_squared_error(Y,predict_score)
RMSE = np.sqrt(MSE)

# show Results 

print("Mean Absolute Error (MAE):",MAE)
print("Mean Squared Error (MSE):",MSE)
print(" Root Mean Absolute Error (RMSE):",RMSE)

# new prediction
# new_hour = float(input("Enter a Hour :"))
# new_pred = model.predict(new_hour)
# print(f"prediction for{new_hour} is score = {new_pred}")

# new_prediction = model.predict([[7]])
# print(f"pred score for 7hr",new_prediction)



