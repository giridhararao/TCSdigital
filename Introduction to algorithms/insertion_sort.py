def insertionsort(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while(i>=0 and a[i]>key):
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return(a)


a=[int(x) for x in input().split()]
print(insertionsort(a))
