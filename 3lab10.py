def duplicate(file):
    content=file.read()
    words=content.split()
    for i in words:
        if words.count(i) >1:
            return("TRUE")
        else:
           return(" FALSE")

file1=open("D:/duplicate.txt")
file2=open('D:/nonduplicate.txt')
print("For duplicate.txt: ",duplicate(file1))
print("For nonduplicate.txt ",duplicate(file2))