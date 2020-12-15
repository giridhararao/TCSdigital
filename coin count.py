a=int(input())
b=[int(x) for x in input().split()]
for i in b:
    count=0
    while(i>=1):
        i=i//2
        count=count+1
    print(count)
