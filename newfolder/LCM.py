def gcd(a,b):
    while(b):
        a,b=b,a%b
    return(a)

def getlcm(a,b):
    return((a*b)/gcd(a,b))

a,b=map(int, input().split())
print(int(getlcm(a,b)))
