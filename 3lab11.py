def hexASCII(l):
    l=list(l)
    d={}
    print("\n","Correspondance between  the  lowercase characters in the"
               " alphabet and the hexadecimal representation of their ASCII code.".upper(),"\n")
    for i in l:
      d[i]= format(ord(i),"x")
    for x,y in d.items():
        print("",x,"    ",y)
hexASCII(input(str("Enter the alphabets to get the hexadecimal representation of their ASCII code: ")))
