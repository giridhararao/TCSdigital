a=int(input())
b=[]
for i in range(a):
    c=[int(x) for x in input().strip().split()]
    b.append(c)
ch=0
c=[]
for i in range(a):
    if(ch==0):
        for j in range(a):
            c.append(b[i][j])
            ch=1
    else:
        for j in range(a-1,-1,-1):
            c.append(b[i][j])
            ch=0
print(*c,sep=" ")
