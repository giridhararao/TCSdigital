import math

def check(a):
        ch=0
        out=[]
        while(a%2==0):
                if(ch>0):
                        return("No")
                else:
                        out.append(2)
                        a=a//2
                        ch+=1
        for i in range(3,int(math.sqrt(a))+1,2):
                ch=0
                while(a%i==0):
                        if(ch>0):
                                return("No")
                        else:
                                out.append(i)
                                ch+=1
                                a=a//i
        if(a>2):
                out.append(a)
        if(len(out)==3):
                return("Yes")
        else:
                return("No")
                        
                

a=int(input())
print(check(a))
