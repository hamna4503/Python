#incomplete reconfirm
m = str(input("Enter the month:").title())
d= int(input("Enter the day:"))
if m=="January"or m=="February"or m=="December":
    print("The season is Winter.")
elif m=="March" or m=="April" or m=="May":
    print('The season is Spring.')

if m=="January" or m=="March" or m=="August" or m=="July"\
    or m=="October" or m=="December":
    if d>31 or d<1:
        print("Invalid date.")
elif m=="June" or m=="April" or m=="September" or m=="N"