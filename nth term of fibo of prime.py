primes=[True for i in range(100001)]
def genprime():
    p=2
    while(p*p<100000):
        if(primes[p]):
            for i in range(p*p,100001,p):
                primes[i]=False
        p+=1

x=int(input())
y=int(input())
genprime()
p=[]
for i in range(x,y+1):
    if(primes[i]):
        p.append(i)
#print(p)
combi=[]
for i in p:
    for j in p:
        if(i!=j):
            c=str(i)+str(j)
            if(primes[int(c)]):
                if(int(c) not in combi):
                    combi.append(int(c))
#print(combi)
#print(len(combi))
co=len(combi)
mi1=min(combi)
ma1=max(combi)
it=1
while(it<co-1):
    c=mi1+ma1
    mi1=ma1
    ma1=c
    it+=1
print(c)
    
