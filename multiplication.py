def multiplication(num):
    res=''
    for i in range(0,11):
        res+=str(num)+'X'+str(i)+'='+str(num*i)+'\n'
    return res
num=int(input("Enter a number:"))
print(multiplication(num))

