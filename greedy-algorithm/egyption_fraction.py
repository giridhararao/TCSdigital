import math

def check(nr,dr):
        out=[]
        while(nr!=0):
                x=math.ceil(dr/nr)
                out.append(x)
                nr=x*nr-dr
                dr=dr*x
        return(out)

nr,dr=map(int,input().split())
out=check(nr,dr)
for i in range(len(out)):
        print("{0}/{1}".format(1,out[i]),end=" ")
