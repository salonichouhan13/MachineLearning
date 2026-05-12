from sklearn.metrics import confusion_matrix
 
# true resuts

Y_true = [1,0,1,1,0,1,0,0,1,0]
Y_pred = [1,0,1,0,0,1,1,0,1,0]

Cm = confusion_matrix(Y_true,Y_pred)
print("Confusion_matrics:")
print(Cm)

# output 
# Confusion_matrics:
# [[4 1]
#  [1 4]]
# 4 True -ve , 1 false +ve
# 1 false -ve , 4 true +ve
