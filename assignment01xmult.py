def xmult(a,b):
    c=[]
    for i in a:
        for j in b:
            c.append(i*j)
    return(c)

l1=[1,2,3,4]
l2=[2,5]
print(l1,"*",l2,"=",xmult(l1,l2))



