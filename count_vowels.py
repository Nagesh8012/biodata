#count vowels

##def countVowels(s):
##    v="aeiouAEIOU"
##    cv=0
##    for i in s:
##        if i in v:
##            cv+=1
##    return cv
##
##s=input("Enter a string:")
##print("Total No of vowels in",s,"is:\n",countVowels(s))
##


def countConsonents(s):
    v="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    cv=0
    for i in s:
        if i in v:
            cv+=1
    return cv

s=input("Enter a string:")
print("Total No of consonents in",s,"is:\n",countConsonents(s))



