def check(a):
        b=[0 for x in range(a+1)]
        if(a==1 or a==0):
                return(1)
        b[0]=1
        b[1]=1
        for i in range(2,a+1):
                b[i]=b[i-1]+b[i-2]
        return(b[a])
a=int(input())
print(check(a))
