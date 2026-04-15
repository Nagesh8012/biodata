###CALCULATOR PROGRAM
##
##def add(a,b):
##    return a+b
##def substract(a,b):
##    return a-b
##def multiply(a,b):
##    return a*b
##def divede(a,b):
##    if b==0:
##        return "Error! Division By zero."
##    return a/b
##
##print("Calculater")
##print("1.Addition")
##print("2.Substration")
##print("3.Multiplication")
##print("4.Devision")
##
##choice=int(input("Enter your choice(1-4):"))
##num1=float(input("Enter first number:"))
##num2=float(input("Enter second number:"))
##
##if choice==1:
##    print("Result:",add(num1,num2))
##elif choice==2:
##    print("Result:",substract(num1,num2))
##elif choice==3:
##    print("Result:",multiply(num1,num2))
##elif choice==4:
##    print("Result:",divide(num1,num2))
##else:
##    print("invalid choice")


#Using signs
###CALCULATOR PROGRAM
##
##def add(a,b):
##    return a+b
##def substract(a,b):
##    return a-b
##def multiply(a,b):
##    return a*b
##def divede(a,b):
##    if b==0:
##        return "Error! Division By zero."
##    return a/b
##
##print("Calculater")
##print("+.Addition")
##print("-.Substration")
##print("*.Multiplication")
##print("/.Devision")
##
##choice=input("Enter your choice(+-*/):")
##num1=float(input("Enter first number:"))
##num2=float(input("Enter second number:"))
##
##if choice=='+':
##    print("Result:",add(num1,num2))
##elif choice=='-':
##    print("Result:",substract(num1,num2))
##elif choice=='*':
##    print("Result:",multiply(num1,num2))
##elif choice=='/':
##    print("Result:",divide(num1,num2))
##else:
##    print("invalid choice")


#using fuctions
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division By zero."
    return a/b
#dictionary acting switch
operations={
    1:add,
    2:substract,
    3:multiply,
    4:divide
}
#calculator logic
print("Calculater")
print("1.Addition")
print("2.Substration")
print("3.Multiplication")
print("4.Devision")

choice=int(input("Enter your choice(1-4):"))

if choice in operations:
    x=float(input("Enter first number:"))
    y=float(input("Enter second number:"))

    result=operations[choice](x,y)
    print("Result:",result)
else:
    print("Invalid choice")
    

