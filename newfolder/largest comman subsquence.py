def lcs(a,b,c,d):
    l=[[0 for x in range(d+1)]for j in range(c+1)]
    for i in range(c+1):
        for j in range(d+1):
            if(i==0 and j==0):
                l[i][j]=0
            elif(a[i-1]==b[j-1]):
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    s=l[c][d]
    out=[""]*(s+1)
    out[s]=""
    row=c
    col=d
    while(row>0 and col>0):
        if(a[row-1]==b[col-1]):
            out[s-1]=a[row-1]
            s-=1
            row-=1
            col-=1
        elif(l[row-1][col]>l[row][col-1]):
            row-=1
        else:
            col-=1
    print(*out,sep="")
            

a=input()
b=input()
lcs(a,b,len(a),len(b))
