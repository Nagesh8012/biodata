def prodDigits(n):
    pd=1
    for i in n:
        pd=pd*int(i)
    return pd
inps=input("Enter a number:")
print(prodDigits(inps))
