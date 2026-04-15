###Factorial
##def factorial(n):
##    if n==0:
##        return 1
##    else:
##        return n*factorial(n-1)
##print('factorial of 3:',factorial(3))


##def factorial(n):
##    if n==0:
##        return 1
##    else:
##        return n*factorial(n-1)
##a=int(input("Enter n no:"))
##print('factorial of'+str(a)+':',factorial(a))


n=(int(input("Enter the Number:")))
if(n==0):
   print(1)
else:
    print(n*factorial(n-1))
print(n)
