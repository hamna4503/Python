import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a ==0:
    print("Cannot be calculated.")
else:
    x = int(-b+(b** 2-(4*a*c))** (1/2))/(2*a), int(-b-(b**2-(4*a*c))**(1/2))/(2 * a)
    print("Hence x =",x)

