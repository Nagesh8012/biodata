def sumDigits(n):
    sd=0
    for i in n:
        sd=sd+int(i)
    return sd
inps=input("Enter a number:")
print(sumDigits(inps))
