# import modules and libraries
from sklearn.linear_model import LogisticRegression


# Input data
X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
y = [0, 0, 1, 1, 1]

## train model
model = LogisticRegression()
model.fit(X, y)

# make prediction
prediction = model.predict([[6,7]])[0]
print(prediction)
