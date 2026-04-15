import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([2,4,5,3,4])
m, b = np.polyfit(x,y,1)

print("Slope =",m)
print("intercept =",b)
print("Equation: y =",m, "x +",b)
