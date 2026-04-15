#check for palindrome

##inps=input('Enter a number or string:')
##rinps=inps[::-1]
##if inps==rinps:
##    print(inps,"is palindrome")
##else:
##    print(inps,"is not palindrome")



def checkPalindrome(inps):
    res=''
    rinps=inps[::-1]
    if inps==rinps:
        res=inps+"is palindrome"
    else:
        res=inps+"is not palindrome"
    return res

inps=input("Enter a number or string:")
print(checkPalindrome(inps))
