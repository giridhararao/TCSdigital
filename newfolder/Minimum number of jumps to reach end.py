def getminsteps(a):
    steps=[0 for x in range(len(a))]
    if(a[0]==0 or len(a)==0):
        return(float('inf'))
    for i in range(1,len(a)):
        steps[i]=float('inf')
        for j in range(i):
            if((i<=j+a[j]) and (a[j]!=float('inf'))):
                steps[i]=min(steps[i],steps[j]+1)
                break
    return(steps[-1])


a=[int(x) for x in input().split()]
print(getminsteps(a))
