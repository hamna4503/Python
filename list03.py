#3.   Write the relevant Python expression or statement,
# involving a list of numbers lst and using
#list operators and methods for these speciﬁcations:
#(a)An expression that evaluates to the index of the middle element of lst
#(b)An expression that evaluates to the middle element of lst
#(c)A statement that sorts the list lst in descending order
#(d)A statement that removes the ﬁrst number of list lst and puts it at the end
#Note: If a list has even length, then the middle element is deﬁned to be the rightmost of
#the two elements in the middle of the list.
lst=[4,5,6,7,3,2,1,8,9]
print("lst:",lst)
#a
if len(lst)%2!=0:
    b=int((len(lst)/2).__ceil__())
    print("a) Index of middle element is: ", b - 1, "\n", "b)The middle element is", lst[b - 1])
else:
    b=int(len(lst)/2)
    print("a) Index of middle element is: ",b, "\n" , "b)The middle element is",lst[b])
#d
a=lst.append(lst.pop(0))
print("d)",lst)
#c
lst.sort()
print("c) Descending order of lst:",lst[::-1])

