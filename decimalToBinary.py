##def DecimalToBinary(d):
##   return bin(d)[2:]
##
##n=int(input("Enter decimal number:"),10)
##print("Equivalent binary number:",decimalToBinary(n))

def decimalToBinary(d):
    d=int(d,10)
    return bin(d)[2:]

n=input("Enter decimal number:")
print("Equivalent binary number:",decimalToBinary(n))
