priamount=int(input())
a=int(input())
b=int(input())
ainterst=[]
outA=0
outB=0
for i in range(b):
        x,y=map(float,input().split(" "))
        square=pow((1+y),(x*12))
        emi=(priamount*y)/(1-1/(square))
        outA=outA+emi

c=int(input())
binterst=[]
for i in range(c):
        x,y=map(float,input().split(" "))
        square=pow((1+y),(x*12))
        emi=(priamount*y)/(1-1/(square))
        outB=outB+emi
if(outA<outB):
        print("Bank A")
else:
        print("Bank B")
