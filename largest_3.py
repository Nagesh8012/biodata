#program to find largest of 3 numbers

##a=float(input("Enter first number:"))
##b=float(input("Enter second number:"))
##c=float(input("Enter third number:"))
##
##if(a>=b)and(a>=c):
##    largest=a
##elif(b>=a)and(b>=c):
##    largest=b
##else:
##    largest=c
##print("The largest number is:",largest)


#function to find the largest of three numbers
def largest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    if b>=a and b>=c:
        return b
    else:
        return c

#main program
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
largest=largest_of_three(num1,num2,num3)
print("The largest number is:",largest)
