def sorli(a,n):
        for i in range(n):
                for j in range(i+1,n):
                        if(a[i]>a[j]):
                                c=a[i]
                                a[i]=a[j]
                                a[j]=c
        return(a)
        
a=int(input())
for i in range(a):
        n=int(input())
        b=[int(x) for x in input().split(" ")]
        b=sorli(b,n)
        #print(b)
        out=b[0]
        x=[]
        out1=0
        j=0
        for i in range(1,n):
                out=out+b[i]
                x.append(out)
                out1=out1+x[j]
                j+=1
        print(out1)
