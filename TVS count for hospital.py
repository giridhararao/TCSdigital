def getpersoncount(D,M):
    return(((6-M)**2)+abs(D-15))

def getval(N,R1,R2,target):
    tvcount=0
    peoplecount=0
    currenttarget=0
    Months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,N+1):
        tvcount=i
        currenttarget=0
        for M in range(1,13):
            for D in range(1,(Months[M])+1):
                peoplecount=getpersoncount(D,M)
                peoplecount=min(N,peoplecount)
                if(peoplecount<=N-tvcount):
                    currenttarget+=peoplecount*R2
                else:
                    currenttarget=currenttarget+(((N-tvcount)*R2)+(peoplecount - (N-tvcount))*R1)
        print(currenttarget,tvcount)
        if(currenttarget>=target):
            break;
    print(tvcount)

N,R1,R2,target=20,1500,1000,7000000
getval(N,R1,R2,target)
