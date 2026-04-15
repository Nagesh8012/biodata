Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("nagesh")
nagesh
print("Good afternoon","Venky")
Good afternoon Venky
x=5
y=6.5
z='mca'
a=[4,'java']
b=(6,7,'year')
c={3:'pen'}
d={6,7,9,"pen"}
e='python'
f='y'
type(x)
<class 'int'>
type(y)
<class 'float'>
==e="python"
SyntaxError: invalid syntax
e="python"
type(z)
<class 'str'>
type(e)
<class 'str'>
type(f)
<class 'str'>
type(a)
<class 'list'>
type(b)
<class 'tuple'>
type(c)
<class 'dict'>
type(d)
<class 'set'>
type(f)
<class 'str'>
type(e)
<class 'str'>
c
{3: 'pen'}
c.keys()
dict_keys([3])
c.values()
dict_values(['pen'])
c.items()
dict_items([(3, 'pen')])
type(d)
<class 'set'>
b=(6,7,'year')
type(b)
<class 'tuple'>
b1=(6)
type(b1)
<class 'int'>
b2=('java')
type(b2)
<class 'str'>
b3=('java',)
type(b3)
<class 'tuple'>
b4=(5,)
type(b4)
<class 'tuple'>
b5=9,'java'
type(b5)
<class 'tuple'>
b6="Naveen",'mca',"python",9,9.8,[6]
type(b6)
<class 'tuple'>
z1=complex(5,8)
z1.real
5.0
z1.img
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    z1.img
AttributeError: 'complex' object has no attribute 'img'. Did you mean: 'imag'?
z1.imag
8.0
e.upper()
'PYTHON'
e.lower()
'python'
a=input()
56
b=input()
java
c=input()
enter a no:
    c=input("Enter a no:")

c=input("Enter a no:")
Enter a no:
99
99
c=input("Enter a no:")
Enter a no:99
d=input("Enter a string:")
Enter a string:mca
type(a)
<class 'str'>
a
'56'
type(a)
<class 'str'>
n1=int(a)
n1
56
n2=list(a)
type(n2)
<class 'list'>
n1=20
n2=6
n1+n2
26
#20+6=26
print(n1,"+",n2,"=",n1+n2)
20 + 6 = 26
print(n1,"+",n2,"=",n1+n2,sep="")
20+6=26
print(n1,"+",n2,"=",n1+n2,sep="#")
20#+#6#=#26
print(str(n1)+"+"+str(n2)+"="+str(n1+n2))
20+6=26
n1
20
n2
6
n1-n2
14
n1/n2
3.3333333333333335
20/2
10.0
n1%n2
2
n1*n2
120
n1//n2
3
2**0.5
1.4142135623730951
2**(1/2)
1.4142135623730951
2**3
8
2**3**2
512
(2**3)**2
64
