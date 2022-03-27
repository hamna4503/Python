provinces=()
for i in range(4):
    p=str(input("Enter province name: ").title())
    provinces=list(provinces)
    provinces.append(p)
print("\n",tuple(provinces))