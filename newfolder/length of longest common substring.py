def lcs(a,b):
        la=len(a)
        lb=len(b)
        li=[[None for i in range(lb+1)]for j in range(la+1)]
        for i in range(la+1):
                for j in range(lb+1):
                        if(i==0 or j==0):
                                li[i][j]=0
                        elif(a[i-1]==b[j-1]):
                                li[i][j]=li[i-1][j-1]+1
                        else:
                                li[i][j]=max(li[i-1][j],li[i][j-1])
        return(li[la][lb])

a=input()
b=input()
print(lcs(a,b))
