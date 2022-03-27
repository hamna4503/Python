#Write a program which will remove 2 friends who left NED.
friends={"Hamna","Aatra","Ramsha","Zara","Bushra"}
for i in range(2):
    l=input("Friend who left NED:").title()
    friends.remove(l)
print("Remaining friends: ",friends)