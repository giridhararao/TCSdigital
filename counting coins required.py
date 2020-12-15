a=int(input())
five=(a-4)//5
if(((a-4)*5)%2==0):
    one=2
else:
    one=1
two=((((a-5)*five)-one)//2)
print(one+two+five, five,two,one)
