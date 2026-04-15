##a=float(input("Enter first number:"))
##b=float(input("Enter second number:"))
##c=float(input("Enter third number:"))
##
##if (a<=b)and(a<=b):
##    smallest=a
##elif(b<=a)and(b<=c):
##    smallest=b
##else:
##    smallest=c
##print('The largeset number is:',smallest)

#fuction
def smallest_of_three(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c

#main function
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter three number:"))
smallest=smallest_of_three(num1,num2,num3)
print("The smallest number:",smallest)
