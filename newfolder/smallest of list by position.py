def quicksort(a):
    length=len(a)
    if(length<=1):
        return(a)
    else:
        leftsqu=[]
        rightsqu=[]
        pivot=a.pop()
        for i in a:
            if(i<pivot):
                leftsqu.append(i)
            else:
                rightsqu.append(i)
        return(quicksort(leftsqu)+[pivot]+quicksort(rightsqu))


n=int(input())
a=[]
for i in range(n):
    c=int(input())
    a.append(c)
po=int(input())
out=quicksort(a)
out1=[]
for i in out:
    if(i not in out1):
        out1.append(i)
print(out1[po-1])



