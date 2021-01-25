import math

def check1(n):
    a=1
    if(n<=1):
        return(1)
    for i in range(2,n+1):
        a*=i
    return(a)

def check(n,p):
    a=check1(n)
    sw=0
    count=0
    while(a%2==0):
        if(p==2):
            count+=1
        a=a//2
    if(p==2):
        return(count)
    for i in range(3,int(math.sqrt(a))+1,2):
        if(sw==1):
            return(count)
        if(i==p):
            sw=1
        while(a%i==0):
            if(i==p):
                count+=1
            a=a//i
    if(a>2):
        if(a==p):
            return(1)
    else:
        return(count)
            


n,p=map(int, input().split())
print(check(n,p))
