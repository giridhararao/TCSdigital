def getval(a):
        num=2*a
        x=num*2
        return(num*(x-1))
        
a=int(input())
b=[]
for i in range(1,a+1):
        b.append(getval(i))
print(*b,sep=" ")
