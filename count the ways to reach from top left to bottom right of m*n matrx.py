#using recursion(it will take more time and space)
def getpath(a,b):
    if(a==1 or b==1):
        return(1)
    else:
        return(getpath(a-1,b)+getpath(a,b-1))

#using math formula
def newgetpath(n,m):
    path=1
    for i in range(n,(m+n-1)):
        path*=i
        path//=(i-n+1)
    return(path)

#using DP it will be better compared to recursion
def dpgetpath(r,c):
    out=[[0 for x in range(r)]for y in range(c)]
    for i in range(c):
        out[0][i]=1
    for j in range(r):
        out[j][0]=1
    for i in range(1,r):
        for j in range(1,c):
            out[i][j]=out[i-1][j]+out[i][j-1]
    return(out[r-1][c-1])
        
a=int(input())
for i in range(a):
    x,y=map(int, input().split())
    #print(newgetpath(x,y))
    print(dpgetpath(x,y))
    #print(getpath(x,y))
