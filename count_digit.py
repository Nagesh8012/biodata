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


def countDigits(s):
    nd=0
    ed=''
    for i in s:
        if i in '0123456789':
            nd+=1
            ed +=i
    return nd,ed

s=input("Enter a string:")
print("Total No of consonents in",s,"is:\n",countDigits(s))



