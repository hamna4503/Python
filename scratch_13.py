str=str(input("Enter msg to be encrypted: "))
encrypt=""
key=int(input("Enter key: "))
for i in str:
    ordinate=ord(i)
    ordinate=ordinate+key
    character=chr(ordinate)
    encrypt+=character

print("Encrypted: ",encrypt)

decrypt=""
for i in encrypt:
    ordinate = ord(i)
    ordinate = ordinate - key
    character = chr(ordinate)
    decrypt += character
print("Decrypted:",decrypt)
