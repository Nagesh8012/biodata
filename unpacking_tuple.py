#Tuple Unpacling allows you to assign each item in an iterable to a variable.

numbers=(1,2,3)
a,b,c=numbers
print("a=",a)
print("b=",b)
print("c=",c)
#A variable that is prefaced with an astrick(*) takes  all values from
#the iterabel that are left over from the other variables.
#a,b,*c,d=[1,2,3,4,6,7,8,9]
a,b,*c,d=(1,'Korivi',3,4,5,6,7,8,9)
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)

#a,b,c,d,*e,f,g=range(20)
#print(len(e))
