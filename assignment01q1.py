grades=[]

a=int(input("How many grades do u wish to input?"))

for i in range(a):
   grades.append(str(input("Enter the grades: ").upper()))

print("LIST: ",grades)

l2=[grades.count("A"),grades.count("B"),grades.count("C"),grades.count("D"),
    grades.count("E"),grades.count("F")]

print("NO. OF OCCURENCES: ",l2)
