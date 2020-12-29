def check(a,b):
    mid=len(a)//2
    if(a[mid]<=b):
        first=0
        last=0
        for i in range(0,mid+1):
            if(a[i]==b):
                first=i
                break
        for j in range(len(a)-1,mid,-1):
            if(a[i]==b):
                last=j+1
                break
        return(last-first)
a=[int(x) for x in input().split()]
b=int(input())
c=check(a,b)
print("%d occurs %d times"%(b,c))
