def printDay(daynum):
    if(daynum==0):
        return"Sunday"
    elif(daynum==1):
        return"Monday"
    elif(daynum==2):
        return"Tuesday"
    elif(daynum==3):
        return"wednesday"
    elif(daynum==4):
        return"Thursday"
    elif(daynum==5):
        return"Friday"
    elif(daynum==6):
        return"Saturday"
    else:
        return"invalid"
dn=int(input("Enter day number"))
print(printDay(dn))
