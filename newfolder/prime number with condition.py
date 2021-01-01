def allprimes(a):
        global primes
        p=2
        while(p*p<a+1):
                if(primes[p]):
                        for i in range(p*p,a+1,p):
                                primes[i]=False
                p+=1

a=int(input())
primes=[True for x in range(a+1)]
primes[0]=False
primes[1]=False
out=[]
out1=[]
allprimes(a)
for i in range(a+1):
        if(primes[i]):
                num=i
                size=len(str(num))
                count=0
                while(num>0):
                        p=num%10
                        if(primes[p]):
                                count+=1
                        num=num//10
                if(count==size):
                        out.append(i)
print(*out,sep=" ")
