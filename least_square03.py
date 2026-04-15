from sklearn.linear_model import LinearRegression
import numpy as np
#data
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])
#model
ob= LinearRegression()
#training
ob.fit(x,y)
# results
print("Slope:", ob.coef_[0])
print('Intercept:', ob.intercept_)
