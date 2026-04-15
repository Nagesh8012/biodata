#python program to remove duplicates
def remove_duplicates(n):
    res=[]
    for i in n:
        if i not in res:
            res.append(i)
    return res
print("input comma seperated numbers:")
inp=list(map(int,input().split(",")))
print(remove_duplicates(inp))
