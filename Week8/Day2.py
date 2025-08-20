# Generator in Python

# def v():
#     yield  24
#     yield 750
#     yield 75
# n = 1
# for i in v():
#     print(i)
#     n = i + i % i
# print()
# print(n)

# l = [x for x in range(0, 10)]
# print(l)


# Closure
# The inner function uses the variable value of the outer function.
#
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
# print(outer(1)(2))


# def outer(m):
#     def inner(x):
#         def inner1(y):
#             def inner2(z):
#                 return x + y / z + m
#             return inner2
#         return inner1
#     return inner
#
# print(outer(25)(1)(3)(9))

# def show(name):
#     def show1(age):
#         def show2(location):
#             # name1 = input("Enter your name: ")
#             # age1 = int(input("Enter your age: "))
#             # location = input("Enter your location: ")
#             return f"My name is {name} i am {age} years old and I live in {location}"
#         return show2
#     return show1
# print(show('Naresh Sadula')(12)('Mumbai'))

# Enumerate Keyword
# data = [1,2,3,4,5]
# for i,j in enumerate(data,start = 1):
#     print(i,j)

# def f1(**kwargs):
#     for i, j in kwargs.items():
#         print("Key = ",i,"Value = ",j)
# f1(name = "Messi",age = 36)

# import pandas as pd
# d = pd.read_csv("data2.csv")
# p = d["Email"]
# str = " "
# for i in p:
#     str+= i + " "
# # print(str)
#
# import re
# v = re.findall("\w[a-z,A-Z]-\d{'com'}]",str)
# print(v)
#
# import pandas as pd
# d = pd.read_csv("data2.csv")
# p = d["Subscription Date"]
# str = " "
# for i in p:
#     str+= i + " "
#
# import re
# v = re.findall("[2022]+\d-\d{2}-\d{2}",str)
# print(v)


# import pandas as pd
# data = pd.read_csv("data2.csv")
# data["FullName"] = data["First Name"] + " " + data["Last Name"]
# print(data["FullName"])

