a,b=map(int, input().split())
c=[int(x) for x in input().split(" ")]
d=[]
for i in range(b):
        x,y=map(int, input().split())
        d.append([x,y])
#print(d)
#print(c)
out=[]
for i in range(b):
        x=d[i][0]
        y=d[i][1]
        out1=[]
        for i in c:
                if(i>=x and i<=y):
                        out1.append(i)
        out.append(len(out1))
print(*out,sep=" ")
