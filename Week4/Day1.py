# String methods in python


# i = s.index("p")

# t = s.title()

# c = s.count("s")

# newS = s.join("Py")

# a = s.isalpha()

# f = s.upper()

# k = s.casefold()

# # print(i)

# # print(t)

# # print(c)

# # print(newS)

# # print(a)

# print(f)

# print(k)

# s = "javascript"
#
# print(s)
#
# t = s.strip()

# g = s.isspace()

# print(g)

# print(t)
#
# print(s.isalpha())

# print(s.upper())

# print(s.isupper())
#
# print(s.islower())
#
# print(s.isascii())
#
# print(s.isdigit())
#
# print(s.isidentifier())
#
# print(s.isalnum())

# Check what does a string contains...
# chr = input("Enter a character: ")
# if chr.isalpha():
#     print(chr, " is an alphabet")
# elif chr.isdigit():
#     print(chr, " is a number")
# else:
#     print(chr, "is a symbol")

# r = "javascript and python"
# print(r.upper())
# print(r.lower())
# print(r.replace("javascript", "java"))
# print(r.find("d"))
# print(r.startswith("j"))
# print(r.endswith("n"))
# print(r.split(" "))
# print(r[:9])

#String Formatting...
# name = "yash"
# age = 2
# s = 'My name is {} and i am {} years old'.format(name,age)
# y = 'My name is {0} and i am {1} months old'.format(name,age)
# print(s)
# print(y)
# print(f'My name is {name} and I am {age} minutes old.')

# Find the count of each alphabet in the string..
# char = input("Enter a String: ")
# l = []
# for i in char:
#     l.append(i)
# f = set(l)
# for j in f:
#     print(j," = ",char.count(j))

# str = "SomeWhere"
# l = list(str)
# print(str.replace("e","a",1))