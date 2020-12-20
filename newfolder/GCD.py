def getgcd(a,b):
    while(b):
        a,b=b,a%b
    return(a)

a,b=map(int, input().split())
print(getgcd(a,b))
