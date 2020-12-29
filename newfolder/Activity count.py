def activity(a,b):
    out=[]
    n=len(b)
    i=0
    out.append(i)
    for j in range(n):
        if(a[j]>=b[i]):
            out.append(j)
            i=j
    return(out)
    
    

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if(b[i]>b[j]):
            temp=b[i]
            temp1=a[i]
            b[i]=b[j]
            b[j]=temp
            a[i]=a[j]
            a[j]=temp1
print(a)
print(b)
out=activity(a,b)
print(len(out))
for i in out:
    print("start -%d and end is %d"%(a[i],b[i]))
