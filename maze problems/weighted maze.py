a=int(input())
b=[]
for i in range(a):
    c=[int(x) for x in input().strip().split()]
    b.append(c)
c=b
for i in range(1,a):
    c[0][i]=max(c[0][i-1],b[0][i])
for j in range(1,a-1):
    c[i][0]=max(c[i-1][0],b[i][0])
for i in range(1,a):
    for j in range(1,a):
        c[i][j]=max(b[i][j],min(c[i][j-1],c[i-1][j]))
print(c[a-1][a-1])
