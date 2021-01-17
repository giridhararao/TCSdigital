def sort(a,b):
        for i in range(len(a)):
                for j in range(i+1,len(a)):
                        if(b[i]<b[j]):
                                b[i],b[j]=b[j],b[i]
                                a[i],a[j]=a[j],a[i]
        return(a,b)

def output(a,b,c):
        big=0
        x=-1
        y=-1
        for i in range(len(a)):
                for j in range(len(a)):
                        if(i!=j):
                                if(big<=(b[i]+b[j]) and ((b[i]+b[j])%c==0)and ((a[x]+a[y])<(a[i]+a[j]))):
                                        big=b[i]+b[j]
                                        x=i
                                        y=j
        if(big==0):
                return(-1)
        else:
                #print(a[x],a[y],big)
                return(a[x]+a[y])
                        

def check(a,b):
        while(b):
                a,b=b,a%b
        return(a)
def check1(a,b):
        out=1
        for i in range(b):
                out*=a
        return(out)
     
n,k,b,m=map(int, input().split())
a=[int(x) for x in input().split()]
power1=[]
for i in a:
        k=0
        for j in range(1,i):
                if(check(j,i)==1):
                        k+=1
        power1.append(check1(k,b))
new1,new2=sort(a,power1)
#print(new1,new2)
print(output(new1,new2,m))
