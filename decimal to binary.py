dec=14
bn="1"
while dec != 1:
    a = dec % 2
    if a == 0:
        bn += "0"
    else:
        bn += "1"
    dec= int(dec / 2)
print(bn)