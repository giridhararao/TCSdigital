def geta1(a):
    v=['a','e','i','o','u','A','E','I','O','U']
    c=""
    for i in a:
        if(i in v):
            c+='%'
        else:
            c+=i
    return(c)

def getb1(a):
    v=['a','e','i','o','u','A','E','I','O','U']
    c=""
    for i in a:
        if(i in v):
            c+=i
        else:
            c+='#'
    return(c)

def getc1(a):
    c=""
    for i in a:
        if(ord(i)>=97 and ord(i)<=122):
            c1=chr(ord(i)-32)
            c+=c1
        else:
            c+=i
    return(c)
            


a1=input()
b1=input()
c1=input()
print(geta1(a1)+getb1(b1)+getc1(c1))
