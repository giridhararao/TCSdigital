a=int(input())
for i in range(1,a+1):
    for j in range(i):
        print(i+2,end=" ")
    print("\r")
for i in range(a,0,-1):
    for j in range(i):
        print(i+2,end=" ")
    print("\r")
