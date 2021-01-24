import math

def check(a):
        out=[]
        while(a%2==0):
                out.append(2)
                a=int(a//2)
        for i in range(3,int(math.sqrt((a)))+1,2):
                while(a%i==0):
                        out.append(i)
                        a=int(a//i)
        if(a>2):
                out.append(a)
        print(*out,sep=" ")
                

a=int(input())
check(a)
