def check(a):
        if(a<=1):
                return(1)
        elif(a==2):
                return(2)
        else:
                return(check(a-1)+check(a-2))
a=int(input())
print(check(a))
