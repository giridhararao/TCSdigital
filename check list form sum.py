def cansum(a,b):
    out=[False for x in range(a+1)]
    out[0]=True
    for i in range(a+1):
        if(out[i]):
            for j in b:
                if(i+j<=a):
                    out[i+j]=True
    return(out[-1])


a=int(input())
b=[int(x) for x in input().split(" ")]
print(cansum(a,b))
