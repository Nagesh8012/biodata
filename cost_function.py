import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticsRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss,confusion_matrix

#2.Load Dataset

data = load_iris()
X = data.data
y = data.target

print("Dataset shape:",X.shape)

#3.

X_train, X_test, y_train, y_test = train_test_split
