def getprim(a):
        p=2
        while(p*p<a+1):
                if(primes[p]):
                        for i in range(p*p,a+1,p):
                                primes[i]=False
                p=p+1

a=int(input())
primes=[True for i in range(a+1)]
primes[0]=False
primes[1]=False
#print(primes)
getprim(a)
#print(primes)
c=[]
for i in range(3,a+1):
        if(primes[i]):
                count=0
                for j in range(i):
                        if(primes[j]):
                                count=count+j
                        if(count==i):
                                print(i)
                                c.append(i)
                                break
print(len(c))             
