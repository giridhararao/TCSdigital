def fitball(a,b):
    #This is for checking the space in hole.
    chsp=[]
    #This is for checking the position of the hole for assiging
    posi=[]
    #This is for storing the hole position where the ball fits.
    bollfit=[]
    for i in range(1,len(a)+1):
        chsp.append(i)
        posi.append(i)
    for i in range(len(b)):
        for j in range(1,len(a)+1):
            # -j is used for itrating from top to down.Input given as down to top.
            if(b[i]<=a[-j] and chsp[-j]!=0):
                bollfit.append(posi[-j])
                chsp[-j]-=1
                break
            if(j==len(a)):
                bollfit.append(0)
                break
    return(bollfit)
#getting the holes diameter as input given from down to high
a=[int(x) for x in input().split()]
#getting the balls diameter
b=[int(x) for x in input().split()]
#print(a)
#print(b)
print(fitball(a,b))
