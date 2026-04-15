#Find unique elements from a list using a set
Ist=[1,2,2,3,4,4,5]
unique=set(Ist)
print("Unique elements:",unique)

#Add an element to a set
s={1,2,3}
s.add(4)
print("Updated set:",s)

#Remove an element from s set
s={1,2,3,4}
s.remove(3)
print("After removal:",s)

#check if an element exists in a set
s={10,20,30}
if 20 in s:
    print("Element found")
else:
    print("Element not found")
    
#find symmetric difference of two sets
#(elements present in either set but not in both)
set1={1,2,3}
set2={3,4,5}
print("Symmetric Difference:",set1^set2)
