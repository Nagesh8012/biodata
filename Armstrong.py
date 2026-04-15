#Armstrong
def checkArmstrong(n):
    n=str(n)
    len_n=len(n)
    s=0
    for i in range(len_n):
        s=s+int(n[i])**len_n
        #print("s=".,s)
    return int(n)==s

for i in range(1000):
    if checkArstrong(i):
        print(i)
