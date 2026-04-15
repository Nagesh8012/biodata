Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
students={ 'alice':85,'bob':92,'charlie':78,'david':90}
students.keys()
dict_keys(['alice', 'bob', 'charlie', 'david'])
students.values()
dict_values([85, 92, 78, 90])
student.item()

students.item()

students.items()
dict_items([('alice', 85), ('bob', 92), ('charlie', 78), ('david', 90)])
help(dict)

a=[33,88,11,99,44]
res=[]
for i in a:
    res.append(i/2)

    
res
[16.5, 44.0, 5.5, 49.5, 22.0]
[i/2 for i in a]
[16.5, 44.0, 5.5, 49.5, 22.0]
x=[22,33,44,55,66]
y=[1,2,3,4,5]
res[]
SyntaxError: incomplete input
for i,j in zip(x,y):
    res.append(i+j)

res
[16.5, 44.0, 5.5, 49.5, 22.0, 23, 35, 47, 59, 71]

for i,j in zip(x,y):
    print('i=',i,'j=',j)

i= 22 j= 1
i= 33 j= 2
i= 44 j= 3
i= 55 j= 4
i= 66 j= 5
[i+j for i in zip(x,y)]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [i+j for i in zip(x,y)]
TypeError: can only concatenate tuple (not "int") to tuple
[i+j for i,j in zip(x,y)]
[23, 35, 47, 59, 71]

========================================== RESTART: M:/Python/high_marks.py =========================================
Highest Marks: 92
Top Student(s): Bob
>>> students={
...     'Alice':85,
...     'Bob':92,
...     'Charlie':78,
...     'David':90
... }
>>> print(students)
{'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
>>> students['Alice']
85
>>> students['Alice']=75
>>> print(students)
{'Alice': 75, 'Bob': 92, 'Charlie': 78, 'David': 90}
>>> students['Nagesh']=33
>>> print(students)
{'Alice': 75, 'Bob': 92, 'Charlie': 78, 'David': 90, 'Nagesh': 33}
>>> k=input()
mahesh
>>> v=int(input())
88
>>> students[k]=v
>>> print(students)
{'Alice': 75, 'Bob': 92, 'Charlie': 78, 'David': 90, 'Nagesh': 33, 'mahesh': 88}
>>> students['Korivi']=33
>>> print(students)
{'Alice': 75, 'Bob': 92, 'Charlie': 78, 'David': 90, 'Nagesh': 33, 'mahesh': 88, 'Korivi': 33}
