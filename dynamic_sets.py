#Create an empty set and add elements
s=set()
s.add(10)
s.add(20)
s.add(30)
print(s)

#find the lenght of a set
s={1,2,3,4,5}
print("Lenght of set:",len(s))

#Remove all elements from a set
s={1,2,3}
s.clear()
print("Set after clear:",s)

#check whether two sets are equal
set1={1,2,3,}
set2={3,2,1}
print("Sets are equal:", set1==set2)

#convert  a string into a set of characters
s='hello'
char_set=set(s)
