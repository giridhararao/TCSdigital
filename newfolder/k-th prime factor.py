import math

def check(a,b):
        ch=0
        while(a%2==0):
                ch+=1
                if(ch==b):
                        return(2)
                a=a//2
        for i in range(3,int(math.sqrt(a))+1,2):
                while(a%i==0):
                        ch+=1
                        if(ch==b):
                                return(i)
                        a=a//i
        if(a>2):
                ch+=1
                if(ch==b):
                        return(a)
        return(-1)
        

a,b=map(int,input().split())
print(check(a,b))
