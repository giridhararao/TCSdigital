def cansum(a,b):
    out=[None for x in range(a+1)]
    out[0]=[]
    for i in range(a+1):
        if(out[i] != None):
            for j in b:
                if(i+j<=a):
                    c=out[i][:]
                    c.append(j)
                    out[i+j]=c[:]
    return(out[-1])


a=int(input())
b=[int(x) for x in input().split(" ")]
print(cansum(a,b))
