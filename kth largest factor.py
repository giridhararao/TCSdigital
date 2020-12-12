a,b=map(int,input().rstrip().split(","))
c=[]
for i in range(1,a+1):
        if(a%i==0):
                c.append(i)
#print the bth highest
print(c[-b])
