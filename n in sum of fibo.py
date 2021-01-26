import sys

def check1(a):
    if(a==0):
        return(0)
    elif(a<=2):
        return(1)
    i,i1,i2=0,1,1
    while(i<=a):
        i=i1+i2
        i1=i2
        i2=i
    return(i1)

def check(a):
    out=[]
    while(a>0):
        b=check1(a)
        out.append(b)
        a=a-b
    print(*out,sep=" ")

a=int(sys.argv[1])
check(a)
