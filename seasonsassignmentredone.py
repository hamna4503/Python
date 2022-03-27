m=str(input("Enter month: ").title())
d=int(input("Enter day: "))
date=""
if m=="January" or m=="March" or m=="August" or m=="July"\
    or m=="October" or m=="December":
    if d>31 or d<1:
        date="Invalid"
    else:
        date="valid"
elif m=="February":
    if d>29:
        date="Invalid"
    else:
        date="valid"
else:
    if d>30:
        date="Invalid"

if date != "Invalid":
    if m=="January"or m=="February" or m=="December":
        print("The season is Winter.")
    elif m=="March" or m=="April"or m=="May":
        print("The season is Spring.")
    elif m=="June" or m=="July" or m=="August":
        print("The season is Summer. ")
    else:
        print("The season is Autumn.")
else:
    print("Invalid date.")



