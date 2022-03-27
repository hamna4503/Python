#.2 Define a list, consisting of names of different students, who are applying for a scholarship
# , pop an
#item from that list and transfer all items in a new list and apply sample method of random module to
#give scholarship to two students of new list.
from random import *
scholarship=["Ali","Ahmed","Sara","Zara","Zohaib","Shakil","Hamid"]
scholarship.pop()
after_pop=[]
after_pop.extend(scholarship)
print("Students applying for scholarship: ",after_pop)
print("Students who got scholarship: ",sample(after_pop,2))
