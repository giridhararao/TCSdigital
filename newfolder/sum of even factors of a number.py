def check(a):
    count=a
    if(a%2!=0):
        print(0)
        return(0)
    for i in range(2,(a//2)+1,2):
        if(a%i==0):
            count+=i
    print(count)
        


a=int(input())
check(a)
