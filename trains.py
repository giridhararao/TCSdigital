a=input()
x,y=a.split(".")
if(x[0]=='0'):
    x=int(x[1])
else:
    x=int(x)
if(y[0]=='0'):
    y=int(y[1])
else:
    y=int(y)
if(not(x>=0 and x<=23 and y>=0 and y<=23)):
    print("Invalid Input")
else:
    a=float(a)
    print("{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format((a+0.00),(a+0.04),(a+0.09),(a+0.15),(a+0.19),(a+0.22)))
