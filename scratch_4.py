def acronym(a):
    h=""
    for i in a.title():
        if i.isupper()==True:
            h=h+i
        else:
            continue
    return h
s=str(input("Enter a phrase: "))
print("The acronym of",s,"is",acronym(s))