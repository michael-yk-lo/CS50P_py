# hello.py
# name = input("What's your name? ")

# Remove whitespace from str, using method .strip()
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()
# name = name.title()

# Combine method
# name = name.strip().title()

# Make it simpler
name = input ("What's your name? ").strip().title()
first, last = name.split(" ")

print("hello, ", name)
print("hello, ")
print(name)

# print (*object, sep = " ", end = "\n")
print("hello, ", name, sep='')
print("hello, ", end="")
print(name)

# escape
print ("hello, \"friend\"")

# fstring
print (f"hello, {first}")