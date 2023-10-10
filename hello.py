#hello.py
name = input("What's your name? ")
print("hello, ", name)
print("hello, ")
print(name)

# print (*object, sep = " ", end = "\n")
print("hello, ", name, sep='')
print("hello, ", end="")
print(name)

# escape
print ("hello, \"friend\"")