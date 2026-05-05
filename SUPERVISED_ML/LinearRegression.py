from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
Y = [40,50,60,70,80]

model = LinearRegression()
model.fit(X,Y)
Hours = float(input("Enter how many hours you studied ="))

predicted_marks = model.predict([[Hours]])
print(f"based on your hours {Hours} you may score arround {predicted_marks}")