"""""""""
7.    Solve the following problem of real world.
A camp of international students has 110 students, as shown in the diagram. The diagram will elaborate that all the students speak some kind of a language. We need to find out how many that speak none of them out of 110 students.
Find how many students speak
a.    English and Spanish but not French?
b.    Neither English, Spanish, nor French?
c.    French, but neither English nor Spanish?
d.    Only one of the three languages?
e.    Exactly two of the three languages?

"""""""""

english={25,17,13,20}
spanish={20,13,19,10}
french={17,13,9,11}
#a
A=sum((english.union(spanish))-french)
print(A)
b=(english.union(spanish).union(french))
print(sum(b))