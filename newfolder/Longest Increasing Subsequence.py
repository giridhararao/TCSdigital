def check(a):
        l=len(a)
        li=[1]*l
        for i in range(1,l):
                for j in range(i):
                        if(a[j]<a[i] and li[i]<li[j]+1):
                                li[i]=li[j]+1
        return(max(li))

a=[int(x) for x in input().split()]
print(check(a))
