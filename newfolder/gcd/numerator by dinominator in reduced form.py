def gcd(a,b):
        while(b):
                a,b=b,a%b
        return(a)

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
num1=1
for i in a:
        num1*=i
num2=1
for i in b:
        num2*=i
c=gcd(num1,num2)
num1=int(num1/c)
num2=int(num2/c)
print(str(num1)+"/"+str(num2))
