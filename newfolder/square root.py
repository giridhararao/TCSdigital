def check(a):
        x=a
        y=1
        e=0.000001
        while(x-y>e):
                x=(x+y)/2
                y=a/x
        return(x)

a=int(input())
print("{:.6f}".format(check(a)))
