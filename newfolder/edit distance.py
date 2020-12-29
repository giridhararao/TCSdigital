def mincheck(a,b):
        out=[[0 for x in range(len(b)+1)]for j in range(len(a)+1)]
        for i in range(len(a)+1):
                for j in range(len(b)+1):
                        if(i==0):
                                out[i][j]=j
                        elif(j==0):
                                out[i][j]=i
                        elif(a[i-1]==b[j-1]):
                                out[i][j]=out[i-1][j-1]
                        else:
                                out[i][j]=1+min(out[i-1][j-1],out[i][j-1],out[i-1][j])
        return(out[len(a)][len(b)])

a=input()
b=input()
print(mincheck(a,b))
