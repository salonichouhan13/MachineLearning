from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# true answers {what actually happend} 

y_true = [1,0,1,1,0,1,0]

# model predicted {what is guessed}

Y_pred = [1,0,1,0,0,1,1]

#evaluate

print("Accuracy:",accuracy_score(y_true,Y_pred))
print("precision:",precision_score(y_true,Y_pred))
print("recall:",recall_score(y_true,Y_pred))
print("f1_score:",f1_score(y_true,Y_pred))

#output
Accuracy: 0.7142857142857143 #accurate 
precision: 0.75 # how many predictions were actualy correct
recall: 0.75 # real positive
f1_score: 0.75  #mixes precision + recall