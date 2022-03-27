#1.   Write a function stats() that takes one input argument: the name of a text file. The
#;function should print, on the screen, the number of lines, words, and characters in the file
#your function should open the file only once
#stats('example.txt') >>>
#line count: 3 word count: 20 character count: 98

def stats(file):
    num_lines = 0
    num_words = 0
    num_chars = 0
    for line in file:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
    print(num_lines)
    print(num_words)
    print(num_chars)

files=open("d:/new.txt","r")
files1=files.read()
(stats(files1))
