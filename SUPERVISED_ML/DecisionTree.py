from sklearn.tree import DecisionTreeClassifier

X = [
  [7,2], #apple
  [8,3], #apple
  [9,1], # orange
  [10,3] #orange
]

Y = [0,0,1,1]  # 0 = apple ,1 = orange
model = DecisionTreeClassifier()
model.fit(X,Y)
Size = float(input("Enter the fruit size in cm = "))
Shade = float(input("Enter the shade of the fruit (1-10) = "))
Result = model.predict([[Size , Shade]])[0]
if Result == 0:
  print("this is likely an apple")
else:
  print("this is likely an orange")
