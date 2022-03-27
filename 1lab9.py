#Write a program which will add your best five students name in a set.
# You will use a loop
#to insert names in set.
s=set()
for i in range(5):
    s.add(input("Enter student name: ").title())
print(s)