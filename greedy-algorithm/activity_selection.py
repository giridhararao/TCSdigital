def sorti(start,finish):
        for i in range(len(finish)):
                for j in range(i+1,len(finish)):
                        if(finish[i]>finish[j]):
                                temp=finish[i]
                                temp1=start[i]
                                finish[i]=finish[j]
                                finish[j]=temp
                                start[i]=start[j]
                                start[j]=temp1
        return(start,finish)

start=[int(x) for x in input().split()]
finish=[int(x) for x in input().split()]
start,finish=sorti(start,finish)
print(start[0],finish[0])
x=finish[0]
i=1
while(i<len(finish)):
        if(start[i]>=x):
                print(start[i],finish[i])
                x=finish[i]
        i+=1
