a,b=(map(int,(input().split())))
b=int(input())
c=[float(x) for x in input().split(" ")]
upt=0
upa=0
downa=0
downt=0
for i in range(0,b-1):
    z=c[i]
    if(z<c[i+1] and upa==0):
        print("up"+str(z)+"  "+str(c[i+1]))
        upt+=1
        upa=1
        downa=0
    else:
        if(z>c[i+1] and downa==0):
            print("Down"+str(z)+"  "+str(c[i+1]))
            downt+=1
            downa=1
            upa=0
print(upt+downt)
