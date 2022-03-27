# 2.   Write a function to design a personal phone directory
# of  your
# parents and friends. You must  add  12  members.
# Then  make  a  function  to  delete  a  member
# from  a  telephone directory. Print total number
# of members in your personal phone directory.

# incomplete as only name del no number are del and also no total
#of member

def direc(name,number):
    d=dict()
    d[name]=d[number]
    return(d)

for i in range(12):
    a=str(input("Enter name: "))
    b=str(input("Enter number: "))
    print(direc(a,b))




