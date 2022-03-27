l1=[2,1,3,5,4,3,8]
l2=[7,9,8,0,4]
print("Original list:",l1)
l1.remove(5)
print("After removing \"5\":",l1)
l1.insert(3,5)
print("Inserting 5 at index 3: ",l1)
l1.sort()
print("After sorting:",l1)
l1.pop()
print("After pop:",l1)
l1.extend(l2)
print("After extending :",l1)
del(l1)
#list has been deleted
