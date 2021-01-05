def gcd(a,b):
        while(b):
                a,b=b,a%b
        return(a)

def lcm(a,b):
        return(int((a*b)/(gcd(a,b))))


a=[int(x) for x in input().split()]

ans=lcm(a[0],a[1])
for i in range(2,len(a)):
        ans=lcm(ans,a[i])
print(ans)
