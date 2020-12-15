a=[int(x) for x in input().split()]
ev=0
od=0
for i in range(0,len(a),2):
    ev=ev+a[i]
for i in range(1,len(a),2):
    od=od+a[i]
if(ev>od):
    print(ev)
else:
    print(od)
