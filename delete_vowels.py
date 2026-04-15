def deleteVowels(s):
    v="aeiouAEIOU"
    res=''
    for i in s:
        if i not in v:
            res +=i
    return res

s=input("Enter a string:")
print("after deleting vowels in",s,"is:\n",deleteVowels(s))

                                                
