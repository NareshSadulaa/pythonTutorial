# Error Handling
# Exception Handling in python
# exception handling means that handle the runtime error using try and except in python.
# There are three types of errors

# 1) Syntax error :- We cannot handle syntax error.
# 2) Logical error :- We can change the code and give the expected output.
# 3) Runtime Error :- We can handle runtime error during runtime using try, except, and finally keyword in python.

# num1 = 2
# num2 = 3
# try:
#     print(num1/num2)
# except:
#     print("error")
#
#
#
# num1 = int(input('Enter a first number: '))
# num2 = int(input('Enter a second number: '))
# try:
#     print(num1/num2)
# except:
#     print('You cannot divide by zero')

# a = [3,5,9]
# while True:
#     ele = int(input('Enter an element to add in list: '))
#     a.append(ele)
#     print(a)

# st = [1,2,3]
# l = [4,5,6]
# try:
#     print(st+l)
# except:
#     print("error")
# finally:
#     print('Program Finished')

# What is data Visualization
# To represent data in diagrams, graphical methods to understand easily
# in python we can perform data visualization using matplotlib
# pip install matplotlib

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,2,1,4]
plt.box(x)
plt.show()