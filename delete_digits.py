def deleteDigits(s):
    d="0123456789"
    res=''
    for i in s:
        if i not in d:
            res +=i
    return res

s=input("Enter a string:")
print("after deleting digits in",s,"is:\n",deleteDigits(s))

