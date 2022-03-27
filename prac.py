###############
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")
##########################
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print("\n")
######################
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")

#Write a program to display all prime numbers within a range
for i in range(25,51):
    if i % 2 != 0 and i % 3 != 0 and  i %  4 !=0 and i % 5!=0 and i % 6!=0 and i % 7!=0\
    and i % 8 !=0 and i %  9 !=0 :
        print(i)
    else:
        continue
for i in range(-10,0,1):
    print(i)

##
l=[10,20,30,40]
l2=reversed(l)
for i in range(3,-1,-1):
    print(l[i])
#Write a Python function to create and print a
# list where the values are square of numbers between 1 and 30 (both included).
def sq(a,b):
    l1=[]
    for i in range(a,b):
        l1.append(i**3)
    return(l1)
print(sq(1,30))
###
for i in range(1,11):
    a=0
    a=i+a
    print(a)
def facto(a):
    for i in range(1,a):
        a=a*i
    return(a)
print(facto(10))
#Write a Python function to multiply all the numbers in a list. Go to the editor
List= [8, 2, 3, -1, 7]
def sulist(l1):
    a=1
    for i in range(len(l1)):
        a=a* l1[i]
    return(a)
print(sulist(List))
#Write a Python function that accepts a string and calculate the number
# of upper case letters and lower case letters.
def stfun(a):
    h=0
    b=0
    for i in (a):
        if i.isupper() == True:
            h=h+1
        else:
            b=b+1
    print("Lowercase:",b,"\n","Uppercase:",h)
s="HEllo I am Hamna"
stfun(s)
##################
a=" "
for i in range(1,11,2):
    print((11 - i) * a, end="")
    for j in range(i):

        print("*","",end="")
    print("\n")
###################
for i in range(1,6):
    if i== 2 :
        print("*")
    elif  i==4:
            print("       ","*")
    else:
        print("*********")
#######################
for i in range(10):
    if i==5 or i==1 or i==9:
        print("*****")
    else:
        print("*   ")
########################
