def check(a,b):
    if(a==0):
        return 1
    out=[0 for i in range(a+1)]
    out[0]=1
    for i in range(1,a+1):
        total=0
        for j in b:
            if((i-j)>=0):
                total+=out[i-j]
        out[i]=total
    return(out[a])
a=int(input())
b=[int(x) for x in input().split()]
print(check(a,b))
