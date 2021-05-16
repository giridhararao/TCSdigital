def checking(x,threecount,twocount):
    threecount
    while(x):
        if(x%3==2):
            threecount+=x//3
            x=2
            twocount+=1
        else:
            threecount+=(x//3)-1
            x=4
            twocount+=2
        break
    return(threecount,twocount)

def check(a):
    if(a<3):
        return(1)
    else:
        c=[]
        x=a//2
        y=a-x
        threecount=0
        twocount=0
        if(x%3==0):
            threecount=x//3
            x=0
        if(y%3==0):
            threecount=y//3
            y=0
        threecount,twocount=checking(x,threecount,twocount)
        threecount,twocount=checking(y,threecount,twocount)
        return((3**threecount)*(2**twocount))
a=int(input())
print(check(a))
