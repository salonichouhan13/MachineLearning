from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5]] #hour studied (input)
Y = [0,0,1,1,1] #result 

model = LogisticRegression()
model.fit(X ,Y)
Hours = float(input("Enter how many hours you studied = "))
Result = model.predict([[Hours]])[0]

if Result == 1:
  print(f"based on hours {Hours} ,you are likely to Pass")
else:
  print(f"based on hours {Hours} ,you are likely to Fail")

