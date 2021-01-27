
def check(a):
        if(a==2):
                return(1)
        elif(a==3):
                return(2)
        if(a%3==0):
                return(pow(3,int(a/3)))
        elif(a%3==1):
                return(4*(pow(3,((int(a/3))-1))))
        elif(a%3==2):
                return(2*pow(3,(int(a/3))))

a=int(input())
print(check(a))
