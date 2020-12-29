def quick(arr):
    if(len(arr)<=1):
        return(arr)
    else:
        pivot=arr.pop()
        left=[]
        right=[]
        for i in arr:
            if(i<pivot):
                left.append(i)
            else:
                right.append(i)
        return(quick(left)+[pivot]+quick(right))

def check(arr,a):
    ceal=-100
    floar=100
    if(a<arr[0]):
        ceal=a[0]
        floar=100000
        return(ceal,floar)
    elif(a>arr[-1]):
        floar=a[-1]
        ceal=-100000
        return(ceal,floar)
    else:
        for i in range(len(arr)-1):
            if(arr[i]<=a and arr[i+1]>=a):
                ceal=arr[i+1]
                floar=arr[i]
                break
    return(ceal,floar)
arr=[int(x) for x in input().split()]
a=int(input())
arr=quick(arr)
ceal,floar=check(arr,a)
if(ceal==-100000):
    print("Floar is %d"%floar)
    print("Ceal is not available")
elif(floar==100000):
    print("Flaor is not available")
    print("Ceal is %d"%ceal)
else:
    print("Floar is %d"%floar)
    print("Ceal is %d"%ceal)
    
