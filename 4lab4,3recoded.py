#recoded verson of 3 lab 3,4
n=(str(input("Enter your name: ").title()))
f=(str(input("Enter your Father's name:").title()))
r=(str(input("Enter your roll number: ")))
subjects=[]
marks=[]
for i in range(5):
    a=subjects.append(str(input("Enter the subject:")))
    b=marks.append(int(input("Enter the marks:")))
print("\n","NAME: ",n,"\n","FATHER'S NAME: ",f,"\n","ROLL NO. :",r)
print("\n","SUBJECTS: ")
for k in subjects:
    print(" ",k.title())
print("\n","MARKS: ")
for h in marks:
    print(" ",h)
pcent=(sum(marks))*100/500
print("\n","PERCENTAGE: ",pcent,"%")
if pcent>=85:
    print(" Grade: A-ONE")
elif pcent>=75:
    print(" Grade: A")
elif pcent>=65:
    print(" Grade: B")
elif pcent>=55:
    print(" Grade: C")
else:
    print(" You have failed.")





