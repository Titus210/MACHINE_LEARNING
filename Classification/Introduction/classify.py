# Clasiffication of iris dataset

# import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

# import Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# split data to training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)

# GAUSSIAN NAIVE BAYES
gnb = GaussianNB()

# train model
gnb.fit(X_train, y_train)

# make predictions
gnb_pred = gnb.predict(X_test)

# print accuracy
accuracyScore = accuracy_score(y_test, gnb_pred)
print(f"Accuracy of Gausian Naive Bayes: {accuracyScore} ")

# DECISION TREE CLASSIFIER
dt = DecisionTreeClassifier(random_state=0)

# train model
dt.fit(X_train, y_train)

# make predictions
dt_pred = dt.predict(X_test)

# print accuracy
accuracy_score = accuracy_score(y_test, dt_pred)
print(f"Accuracy of Decision Tree: {accuracyScore} ")

# SUPPORT VECTOR MACHINE
svm_clf = svm.SVC(kernel='linear')
# train the model
svm_clf.fit(X_test, y_test)
# prediction
svm_pred = svm_clf.predict(X_test)
svn_accuracy = accuracy(y_test, svm_pred)
print(f"Accuracy of support vector machine: {accuracyScore} ")


