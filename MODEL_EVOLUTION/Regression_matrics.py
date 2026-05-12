from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np 

# real score 
real_score = [90,60,80,100]
#model predicts
predicted_score = [85,70,70,95]

MAE = mean_absolute_error(real_score,predicted_score)
MSE = mean_squared_error(real_score,predicted_score)

RMSE = np.sqrt(MSE)

print("MAE : on avrg off by:", MAE)
print("MSE : squared mistake value:", MSE)
print("RMSE : final realistic error:", RMSE)

#ouputs
# MAE : on avrg off by: 7.5
# MSE : squared mistake value: 62.5
# RMSE : final realistic error: 7.905694150420948