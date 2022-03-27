def make_list(number_of_families):
    l={}
    lst=[]
    for i in range(number_of_families):
        print(" ")
        x=input(str(("Enter Family name: ")))
        n=int(input("Enter number of family members: "))
        for j in range(n):
            lst.append(input("Enter family members: "))
        l[x]=lst
    return(l)

def common_guests(a,b):
    number=0
    lst=[]
    for x,y in a.items():
        for i,j in b.items():
            if x==i:
                for k in y:
                    for l in j:
                        if k==l:
                            if k not in lst:
                                lst.append(k)
                                number += 1
                            else:
                                continue
    print("Members: ",lst,"\n","Number of common members: ",number)

print("PARENT'S LIST:")
parents_list = make_list(3)
print("MY GUEST LIST: ")
my_list = make_list(2)
print("PARENT's LIST",parents_list,"\n","MY GUEST LIST",my_list)
print("\n","COMMON GUESTS:")
common_guests(parents_list,my_list)










