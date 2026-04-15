import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,3,5,4,5])
ob = LinearRegression()
ob.fit(x,y)
#predictions
y_pred = ob.predict(x)
#plot
plt.scatter(x,y)
plt.plot(x, y_pred)

plt.xlabel('X values')
plt.ylabel("y values")
plt.title("Linear Square Linear Regression")
plt.show()
#Dots --actual dataset poits
#line -- best-fit regrssion line calculated using Least Squares
