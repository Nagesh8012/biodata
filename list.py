Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=list()
b[]

b=[]
c=list('apple')
d=list(23)

d=[23,89.4,'apple','c']
type(a)
<class 'list'>
type(b)
<class 'list'>
type(c)
<class 'list'>
type(d)
<class 'list'>
e=list([7,99,8])
e
[7, 99, 8]
f=list((5,8,9))
f
[5, 8, 9]
help(list)

temp=[56,89,34]
print(temp)
[56, 89, 34]
temp.append(23)
print(temp)
[56, 89, 34, 23]
temp.append(6.8)
print(temp)
[56, 89, 34, 23, 6.8]
temp.append('cr')
print(temp)
[56, 89, 34, 23, 6.8, 'cr']
temp.append([44,55,11])
print(temp)
[56, 89, 34, 23, 6.8, 'cr', [44, 55, 11]]
temp[0]
56
temp[1]
89
temp(6)

temp[6]
[44, 55, 11]
temp[-1]
[44, 55, 11]
temp[-2]
'cr'
temp.append((44,55))
print(temp)
[56, 89, 34, 23, 6.8, 'cr', [44, 55, 11], (44, 55)]
len(temp)
8
temp.clear()
print(temp)
[]
a=[56, 89, 34, 23, 6.8, 'cr', [44, 55, 11], (44, 55)]
a[6]
[44, 55, 11]
a[6][0]
44
a[6][1]
55
a[6][2]
11
a[6][0]='python'
a
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11], (44, 55)]
a[7][0]=77
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a[7][0]=77
TypeError: 'tuple' object does not support item assignment
a
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11], (44, 55)]
del a[-1]
a
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11]]
b=a
b
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11]]
id(a)
2351343812672
id(b)
2351343812672
b.append('prashu')
b
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11], 'prashu']
a
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11], 'prashu']
c=a.copy()
id(c)
2351343974208
del a[-1]
 a
 
SyntaxError: unexpected indent
a
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11]]
b
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11]]
c
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11], 'prashu']
a.append(89)
a.append(89)
a.append('cr')
a
[56, 89, 34, 23, 6.8, 'cr', ['python', 55, 11], 89, 89, 'cr']
a.count(34)
1
a.count('cr')
2
a.count('mca')
0
help(list.count)
Help on method_descriptor:

count(self, value, /)
    Return number of occurrences of value.

b=[56,89,'cr']
b.extend(['gua','papaya'])
b
[56, 89, 'cr', 'gua', 'papaya']
b.extend('crt')
b
[56, 89, 'cr', 'gua', 'papaya', 'c', 'r', 't']
b.index('cr')
2
b.index('mca')

b.insert(0,'mca')
b
['mca', 56, 89, 'cr', 'gua', 'papaya', 'c', 'r', 't']
b.insert(-1,'mca')
b
['mca', 56, 89, 'cr', 'gua', 'papaya', 'c', 'r', 'mca', 't']
b.insert(3,'games')
b
['mca', 56, 89, 'games', 'cr', 'gua', 'papaya', 'c', 'r', 'mca', 't']
x=b.pop()
x
't'
b
['mca', 56, 89, 'games', 'cr', 'gua', 'papaya', 'c', 'r', 'mca']
x=b.pop(3)
x
'games'
b.reverse()
b
['mca', 'r', 'c', 'papaya', 'gua', 'cr', 89, 56, 'mca']
xb.reverse()

x=b.reverse()
x
b
['mca', 56, 89, 'cr', 'gua', 'papaya', 'c', 'r', 'mca']
c=[67,89,44,11,22]
c.sort(reverse=True)
c
[89, 67, 44, 22, 11]
#sort a string
s=input()
good morning
>>> s
'good morning'
>>> a=list(s)
>>> a
['g', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g']
>>> a.sort()
>>> a
[' ', 'd', 'g', 'g', 'i', 'm', 'n', 'n', 'o', 'o', 'o', 'r']
>>> "".join(a)
' dggimnnooor'
>>> '#'.join(a)
' #d#g#g#i#m#n#n#o#o#o#r'
>>> ''.join(a)
' dggimnnooor'
>>> ' '.join(a)
'  d g g i m n n o o o r'
>>> data=[['prasad',36,38],['madhu',35,39],['venky',28,29],['jeevana',40,12]]
>>> data
[['prasad', 36, 38], ['madhu', 35, 39], ['venky', 28, 29], ['jeevana', 40, 12]]
>>> data.sort(key= lambda x:x[1])
>>> data
[['venky', 28, 29], ['madhu', 35, 39], ['prasad', 36, 38], ['jeevana', 40, 12]]
>>> data.sort(key= lambda x:x[2])
>>> data
[['jeevana', 40, 12], ['venky', 28, 29], ['prasad', 36, 38], ['madhu', 35, 39]]
>>> data.sort(key= lambda x:x[1],reverse=True)
>>> data
[['jeevana', 40, 12], ['prasad', 36, 38], ['madhu', 35, 39], ['venky', 28, 29]]
>>> data.sort(key= lambda x:(x[1]+x[2])/2)
>>> data
[['jeevana', 40, 12], ['venky', 28, 29], ['prasad', 36, 38], ['madhu', 35, 39]]
