a=int(input())
b=[]
for i in range(3):
    c=[x for x in input().split()]
    b.append(c)
print(b)
out=""
i=0
while(i<a):
    print(i)
    if(b[0][i]=='#'):
        out=out+'#'
        i=i+1
        continue
    elif(b[0][i]=='.' and b[2][i]=='.' and b[2][i]=='.'):
        i=i+1
        continue
    elif(i<a-2 and b[0][i]=='.' and b[0][i+2]=='.' and b[2][i+1]=='.'):
        out+='A'
        i=i+3
        continue
    elif(i<a-1 and b[0][i+1]=='.' and b[1][i+1]=='.'):
        out+='U'
        i=i+3
        continue
    elif(i<a-1 and b[1][i+1]=='.'):
        out+='O'
        i=i+3
        continue
    elif(i<a-2 and b[1][i]=='.' and b[1][i+2]):
        out+='I'
        i=i+3
        continue
    else:
        out+='E'
        i=i+3
        continue
print(out)
