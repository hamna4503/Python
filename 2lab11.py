def direc(a):
    d = dict()
    for i in range(a):
        name=str(input("Enter name: "))
        number= int(input("Enter number: "))
        d[name]=number
    return(d)

directory=(direc(12))
print("Original directory : ","\n","Name","\t","Numbers")
for i,j in directory.items():
    print(i,j,"\n")
def delete(a):
    if a in directory.keys():
        directory.pop(a)
        return(directory)

to_del="hamna"
print("\n","After deleting",to_del,"from directory: ",delete(to_del))

print("\n","Total members: ",len(directory))

