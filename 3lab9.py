dish=set()
num=int(input("Input the number of dishes u wish to enter: "))
for i in range(num):
    dish.add(input("Enter dish: "))
print("Best dishes: ",dish)
for i in range(len(dish)):
    dish.pop()
    print("After",i+1,"pop: ",dish)