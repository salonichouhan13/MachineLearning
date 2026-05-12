import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import matplotlib.pyplot as plt

# load dataset 

data = pd.read_csv("PROJECTS/student_performance.csv")

# input and output 

X = data[["StudyHours"]]
Y = data["ExamScore"]

# train model 
model = LinearRegression()
model.fit(X,Y)
predicted_score = model.predict(X)

# valid regression metrics

MAE = mean_absolute_error(Y,predicted_score)
MSE = mean_squared_error(Y,predicted_score)
RMSE = np.sqrt(MSE)
r2 = r2_score(Y,predicted_score)

# show results 

print("Mean Absolute Error (MAE):",round(MAE,2))
print("Mean Squared Error (MAE):",round(MSE,2))
print(" Root Mean squared Error (MAE):",round(RMSE,2))
print("r2 score(model accuracy):",round(r2,4))

# histogram 
# plt.figure(figsize=(10,6))
# plt.hist(data["ExamScore"],bins=30, color="skyblue", edgecolor = "black" )
# plt.title("Distribution of final exam score")
# plt.xlabel("Final Exam Score")
# plt.ylabel("Number Of Students")
# plt.grid(True)
# plt.show()

# scatter plot regression line
plt.figure(figsize=(10,6))
plt.scatter(X,Y, color="blue", label = "Actual Score" )
plt.plot(X,predicted_score,color = "red" ,label = "Regression Line")
plt.title("Model Prediction vs Actual Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Output")
plt.grid(True)
plt.show()

new_hr = 9
predicted_new_score = model.predict([[new_hr]])
print(f"Predicted Final Score For{new_hr} hours is {predicted_new_score}")