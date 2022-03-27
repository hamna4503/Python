#1.   Write a function stats() that takes one input argument: the name of a text file. The
#;function should print, on the screen, the number of lines, words, and characters in the file
#.your function should open the file only once
#stats('example.txt') >>>
#line count: 3 word count: 20 character count: 98


def stats(a):
    lines=0
    character=0
    h=0
    for i in a:
        if i!="\n":
            lines+=1
        j=i.split()
        character+=1
        for k in j:
            x=len(k)
            h+=x
    print(lines,character,h)


b=open("ab.txt")
stats("ab.txt")
b.close()




