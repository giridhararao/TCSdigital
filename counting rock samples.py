a=[345,604,321,433,704,470,808,718,517,811]
b=[[300,380],[400,700]]
k=-1
c=[]
for i in b:
    k+=1
    c.append(0)
    for j in a:
        if(j>=i[0] and j<=i[1]):
            c[k]+=1
print(*c,sep=" ")
