def check(a):

        nextpostion=a
        if(check.counter>a):
                return(1)
        if(a%check.counter==0):
                return(0)
        nextpostion=nextpostion-nextpostion//check.counter
        check.counter+=1
        return(check(nextpostion))


a=int(input())
check.counter=2
if(check(a)):
        print("Lucky number")
else:
        print("Not lucky number")
