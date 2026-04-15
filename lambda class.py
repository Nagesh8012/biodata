Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=lambda x,y:x+y
a(6,11)
17
f=lambda a,b:3*a**2+5*b+11
f(2,3)
38
w=[2,1,0,7,9,4,3,2,3]
#[4,1,0,49,81,16,9,4,9]
map(lambda a:pow(a,2),w)
<map object at 0x000001C8B436C880>
for i in map(lambda a:pow(a,2),w):print(i)

4
1
0
49
81
16
9
4
9
list(map(lambda a:pow(a,2),w))
[4, 1, 0, 49, 81, 16, 9, 4, 9]
def square(a):return a**2

list(map(a,w))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(map(a,w))
TypeError: <lambda>() missing 1 required positional argument: 'y'
w=[2,1,0,7,9,4,3,2,3]
w=[2,1,0,7,9,4,3,2,3]
##[4,1,0,49,81,16,9,4,9]
map(lambda a:pow(a,2),w)
<map object at 0x000001C8B436D450>
for i in map(lambda a:pow(a,2),w))
SyntaxError: unmatched ')'
for i in map(lambda a:pow(a,2),w):print(i)

4
1
0
49
81
16
9
4
9
list(map(lambda a:pow(a,2),w))
[4, 1, 0, 49, 81, 16, 9, 4, 9]
w
[2, 1, 0, 7, 9, 4, 3, 2, 3]
def square(a):return a**2

square(11)
121
list(map(square,w))
[4, 1, 0, 49, 81, 16, 9, 4, 9]
def sr(x):return x**0.5

sr(9)
3.0
w
[2, 1, 0, 7, 9, 4, 3, 2, 3]
r=list(map(sr,w))
r
[1.4142135623730951, 1.0, 0.0, 2.6457513110645907, 3.0, 2.0, 1.7320508075688772, 1.4142135623730951, 1.7320508075688772]
def sr(x):return round(x**0.5,2)

sr(9)
3.0
r=list(map(sr,w))
r
[1.41, 1.0, 0.0, 2.65, 3.0, 2.0, 1.73, 1.41, 1.73]
w
[2, 1, 0, 7, 9, 4, 3, 2, 3]
r=list(map(lambda a:round(a**(1/3),2),w))
e

r
[1.26, 1.0, 0.0, 1.91, 2.08, 1.59, 1.44, 1.26, 1.44]
#input:
#3,5
#8
#input:
>>> #apple,gua,man,papaya
>>> #5,3,3,6
>>> input()
apple,gua,man,papaya
'apple,gua,man,papaya'
>>> input().split(",")
apple,gua,man,papaya
['apple', 'gua', 'man', 'papaya']
>>> 'apple,gua,man,papaya'.split(",")
['apple', 'gua', 'man', 'papaya']
>>> '5,3,3,6'.split()
['5,3,3,6']
>>> print(list(map(len,input().split(","))))
apple,gua,man,papaya
[5, 3, 3, 6]
>>> print(*list(map(len,input().split(","))))
apple,gua,man,papaya
5 3 3 6
>>> #['5','3','3','6']
>>> #[5, 3, 3, 6]
>>> n=['5','3','3','6']
>>> list(map(int,n))
[5, 3, 3, 6]
>>> list(map(len,input().split(",")))
list(map(int,input().split(",")))
[12, 15, 4]
>>> sum(list(map(int,input().split(","))))
5,3,3,6
17
