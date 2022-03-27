items={"Lotion","Soap","Face Wash","Shampoo","Perfume"}
print("ITEMS: ",items)
num=int(input("Enter number of items u would like to "
              "purchase"))
l=[]
price_list=[]
purchase_list=[]
for i in range(num):
    purchase=str(input("Enter the item u want to purchase: ").title())
    purchase_list.append(purchase)
    n=int(input("Enter the number of this item you want: "))
    l.append(n)
    if purchase in items:
        items.remove(purchase)
        if purchase=="Lotion":
            price=400*n
        elif purchase=="Soap":
            price=300*n
        elif purchase=="Face Wash":
            price=650*n
        elif purchase=="Shampoo":
            price=100*n
        elif purchase=="Perfume":
            price=800*n
        price_list.append(price)
    else:
        print("Sorry the item is not available.")
print("ITEM      PRICE")
for i in range(len(purchase_list)):
     print(" ",purchase_list[i],"      ",price_list[i])
print("\n")
print("YOUR TOTAL IS: ",sum(price_list))
print("YOUR TOTAL ITEMS ARE: ",sum(l))
print("REMAINING ITEMS ARE:",items)
print("MAXIMUM NUMBER OF ITEMS:",max(l))
print("MINIMUM NUMBER OF ITEMS:",min(l))







