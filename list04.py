#Start by assigning to variables monthsL and monthsT a list and a tuple, respectively,
# both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order.
# Then attempt the following with both containers:
#(a)Insert string 'Apr' between 'Mar' and 'May'.
# (b)Append string 'Jun'.
#(c)Pop the container.
#(d)Remove the second item in the container.
# (e)Reverse the order of items in the container.
#f) sort the container
monthsT=("Jan","Feb","Mar","May")
print("monthsT: ",monthsT)
#a
#b

monthsT.pop()
print("c) After pop(): ",monthsT)
#d
monthsT.remove("Mar")
print("d) After removing \'Mar\': ",monthsT)
#e
print("e) Reverse tuple: ",monthsT[::-1])
#f
monthsT.sort()
print("f) After sorting: ",monthsT)

