#program to check whether a given is a leap year or not
'''
A year is a leap year if:
_it is divisible by 4
-But if it is devisilble by 100, it must also be divisible by 400
'''
#function check a leaf year
def is_leap_year(year):
    if(year%400==0):
        return True
    elif(year%100==0):
        return True
    elif(year%4==0):
        return True
    else:
        return False
year=int(input("Enter the year :"))
if is_leap_year(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
    
