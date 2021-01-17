def gcd(a,b):
        while(b):
                a,b=b,a%b
        return(a)

def check(a):
        out=0
        for i in range(len(a)):
                for j in range(len(a)):
                        z=gcd(a[i],a[j])
                        if(i!=j and (z>out)):
                                out=z
        print(out)
                                

a=[int(x) for x in input().split()]
check(a)
