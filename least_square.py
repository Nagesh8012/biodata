import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([1,7,3,5,5])
n=len(x)
sum_x=sum(x)
sum_y=sum(y)
print("sum_x=",sum_x)
print("sum_y=",sum_y)
sum_xy = 0
sum_x2 = 0
for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]
print("sum_x=",sum_xy)
print("sum_y=",sum_x2)
#calculate slope (m)
m= (n* sum_xy - sum_x * sum_y) / (n * sum_x2 -sum_x**2)
#calculate intercept (b)
b= (sum_y - m* sum_x) / n
print("Slope (m) =", m)
print("Intercept (b) =", b)
print("\nRegression Equation:")
print("y=",m,"x+",b)
