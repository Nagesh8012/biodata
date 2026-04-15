Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import builtins
dir(builtins)

a=5
id(a)
140706948041272
hex(id(a))
'0x7ff8e3a7ca38'
b=9
id(9)
140706948041400
c=b-4
c
5
id(c)
140706948041272
b
9
b=b-4
b
5
id(b)
140706948041272
n1=20
n2=22
n3=4
n1+n2
42
n1-n2
-2
n1*n3
80
n1/n2
0.9090909090909091
n1/n3
5.0
n1//n3
5
n1%n3
0
n2%n3
2
20+4
24
'tewnty'+4

'twenty'+'four'
'twentyfour'
2**3
8
2**3**2
512
2**(1/2)
1.4142135623730951
'Nagesh'*3
'NageshNageshNagesh'
3*'nagesh'
'nageshnageshnagesh'
z='apple'
z=7
#numbers,strings,list,tuples,dictionary,set
#int()
a=2**.5
a
1.4142135623730951
round(a,3)
1.414
round(a,2)
1.41
round(a)
1
#int()
a=int()
a
0
b=int(7)
b
7
c=int('9')
c
9
d=int('101',2)
d
5
>>> e=int('101',3)
>>> x=int('101',3)
>>> x
10
>>> e=int('132',2)

>>> f=int('789'10)

>>> f=int('789',10)
>>> f
789
>>> g=int('789')
>>> g
789
>>> help(int)

>>> bin(5)
'0b101'
>>> bin(5)[2:]
'101'
>>> oct(40)
'0o50'
>>> hex(40)
'0x28'
>>> bin(5)[4:]
'1'
