#print Factors
def checkPrime(n):
    res=[]
    for i in range(1,n+1,1):
        if n%i==0:
            res.append(i)
    return "PRIME" if len(res)==2 else "NOT PRIME"
a=int(input(),10)
print(checkPrime(a))

   





##n=int(input())
##res=[]
##for i in range(1,n+1,1):
##    if n%i==0:
##        res.append(i)
##print(res)
##print(len(res))
