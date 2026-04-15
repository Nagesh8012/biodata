from functools import reduce

#define a list
#numbers=[1,2,3,4,5]
numbers=list(map(int,input().split(",")))#user input
#use reduce to find the sum
total_sum=reduce(lambda x,y:x+y,numbers)

#print the result
print("Sum of the list:",total_sum)
