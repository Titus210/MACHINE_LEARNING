# Clasiffication of iris dataset

# import libraries
import numpy as np
import panda as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

## import Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# split data to training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

# GAUSSIAN NAIVE BAYES


