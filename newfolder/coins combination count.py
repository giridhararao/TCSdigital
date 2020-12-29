def checkmin(a,b):
        out=[0 for x in range(a+1)]
        out[0]=1
        for i in b:
                for j in range(i,a+1):
                        out[j]+=out[j-i]
        return(out[-1])

a=int(input())
b=[int(x) for x in input().split()]
print(checkmin(a,b))
