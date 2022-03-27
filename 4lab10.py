def abc():
    filename = input("Enter name of file: ")
    file1 = open(filename, 'w')
    for i in file1:
        if len(i)==4:
            i.replace("xxxx")
        else:
            continue
abc()

