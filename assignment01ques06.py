n = int(input("Enter number of students: "))
l1 = []

for j in range(n):
    l1.append(input(str("Enter name of students:")).title())
print("List:", l1, "\n", "Names through A to M:")

for i in l1:
    if i[0] == "A" or i[0] == "B" or i[0] == "C" or i[0] == "C" or i[0] == "D" or \
            i[0] == "E" or i[0] == "F" or i[0] == "G" or i[0] == "H" or i[0] == "I"\
            or i[0] == "J" or i[0] == "L" or i[0] == "M":
        print(i)
    else:
        continue
