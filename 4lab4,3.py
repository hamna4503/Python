#recheck code and recode

name=str(input("Enter your name: "))
fname=str(input("Enter your Father's name: "))
rno=input("Enter your roll number: ")
s1=str(input("Enter first subject: "))
m1=int(input("Enter marks of the subject:"))
s2=str(input("Enter second subject : "))
m2=int(input("Enter marks of the subject:"))
s3=str(input("Enter third subject: "))
m3=int(input("Enter marks of the subject:"))
s4=str(input("Enter fourth subject: "))
m4=int(input("Enter marks of the subject:"))
s5=str(input("Enter fifth subject: "))
m5=int(input("Enter marks of the subject:"))
pcent=(m1+m2+m3+m4+m5)*100/500
print("\n")
print(" RESULT:","\n\n","Name: ",name.title(),"\n","Father's name: ",fname.title(),"\n","Roll number:",rno)
print("\n","SUBJECTS","AND","MARKS OBTAINED","\n",s1.title(),": ",m1,"\n",s2.title(),": ",m2,"\n",s3.title(),": ",m3)
print("",s4.title(),": ",m4,"\n",s5.title(),": ",m5,"\n")
print(" Percentage: ",pcent,"%")
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

