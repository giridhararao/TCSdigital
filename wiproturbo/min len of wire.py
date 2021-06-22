n=int(input())
light=[int(x) for x in input().split()]
distance=[int(x) for x in input().split()]
sum=0
for i in range(n):
    if(light[i]==0):
        pre=distance[i]-distance[i-1]
        if(i<n-1 and light[i+1]==1):
            post=distance[i+1]-distance[i]
            if(pre<post):
                sum+=pre
            else:
                sum+=post
        sum+=pre
print(sum)
