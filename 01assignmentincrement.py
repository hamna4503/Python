#making function
def increment(salary,gradescale):
    if gradescale >=1 and gradescale<15:
        per=20
    if gradescale >=15 and gradescale<20:
        per=10
    if  gradescale >= 20 and gradescale< 22:
        per = 5
    updated = salary * per/100
    updated = updated+salary
    return (updated)

#calling the function
s=float(input("Enter the salary: "))
g=float(input("Enter the grade scale:  "))
print("The updated salary is",increment(s,g))


#calling the function -- give random comment to reflect on github



