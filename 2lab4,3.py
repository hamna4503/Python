n = int(input("Enter the no. of term : "))
a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
tn= a + ((n-1)*d)
print("The",n,"th","term is",tn)
print("\n")
proceed= str(input("Do u wish to find another term(y/n)"))
print("\n")
while proceed =="y" or proceed== "Y":
    n = int(input("Enter the no. of term : "))
    a = int(input("Enter the first term: "))
    d = int(input("Enter the common difference: "))
    T = a + ((n - 1) * d)
    print("The", n, "th", "term is", T)
    print("\n")
    proceed = str(input("Do u wish to find another term(y/n)"))
    print("\n")




