# Area of a traingle

##import math
##def calculateArea(b,h):
##    return 0.5*b*h
##b=int(input("Enter base value:"))
##h=int(input("Enter height value:"))
##print(calculateArea(b,h))

#area find one by fourth
import math
def areaOne(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Enter three sides of a traingle:")
a=float(input())
b=float(input())
c=float(input())
print(areaOne(a,b,c))
