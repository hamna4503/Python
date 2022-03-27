
a=" "
i=1
while i<=8:
   if i<5:
    for j in range(15):
        print("*",end="")
   else:
      print(15*a,end="")
      for j in range(15):
          print("*",end="")
   print()
   i+=1
