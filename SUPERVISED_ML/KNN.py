from sklearn.neighbors import KNeighborsClassifier 

X = [
  [180,7],
  [200,5],
  [250,8],
  [300,8.5],
  [330,9],
  [360,9.5]
]

# 0= apple , 1 =  orange
Y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X ,Y)
Weight = float(input("Enter the weight in gm = "))
Size = float(input("Enter the size in cm = "))

prediction = model.predict([[Weight,Size]])[0]

if prediction == 0:
  print("this is likely an apple")
else:
  print("this is likely an orange")


