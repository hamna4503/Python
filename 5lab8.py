message='The secret of this message is that it is secret.'
length=len(message)
count=message.count("secret")
censored=message.replace("secret","xxxxx")

print("a) message= ",message)
print("b) length= ",length)
print("c) count= ",count)
print("d) censored= ",censored)
