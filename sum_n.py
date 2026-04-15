#Print the sum of the first N natural numbers
def sum_natural(n):
    return n*(n+1)//2
n=int(input("Enter a number:"))
print("Sum of first","natural numbers is:", sum_natural(n))


###fuction
##def sum_n(n):
##    if n==0:
##        return 0
##    else:
##        return n+sum_n(n-1)
##n=int(input("Enter a number:"))
##print("Sum=",sum_n(n))


#anothe method using Loops
n=int(input("Enter a number:"))
s=0
for i in range(1,n+1,1):
    s +=i #s=s+i
print("Sum of first ",n,"natural numbers is",s)
