def getsmall(a):
    if(a<10):
        return(a+10)
    out=[]
    for i in range(9,1,-1):
        while(a%i==0):
            a=a//i
            out.append(i)
    if(a>10):
        return("Not Possible")
    n=out[-1]
    for i in range(len(out)-2,-1,-1):
        n=10*n+out[i]
    return(n)


a=int(input())
print(getsmall(a))
