import math


def check(a,b):
        out=[]
        count=0
        while(a%2==0):
                out.append(2)
                a=a//2
                count+=2
        for i in range(3,int(math.sqrt(a))+1,2):
                while(a%i==0):
                        out.append(i)
                        count+=i
                        a=a//i
        if(a>2):
                if(a>10):
                        c=check1(a)
                        out.append(c)
                        count+=c
                else:
                        out.append(a)
                        count+=a
        if(len(out)==1):
                print("No")
        else:
                if(count==b):
                        print("Yes")
                else:
                        print("No")

def check1(b):
        count=0
        while(b!=0):
                count+=b%10
                b=b//10
        return(count)
                

a=int(input())
b=check1(a)
check(a,b)
