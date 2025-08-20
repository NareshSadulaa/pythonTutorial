# There are two types of Loops
# 1)For Loop
# 2)While Loop

# Syntax:-
# seq:- range(start,stop,step) list,tuple,string,dictionary,set
# for variable in seq:
#     statements

# Increment:-
# for i in range(10,20):
#     print(i)
#
# Decrement:-
# for i in range(20,10,-1):
#     print(i)

# String without using variable
for i in "MESSI":
    print(i)
#
# Dictionary With Variable
# a = {1:3,2:4,3:5,4:6,5:7}
# for i in a:
#     print(i)

# Dictionary Without using Variable
# for i in {1:2,3:4,5:6}:
#     print(i)

# List with variable
a = [1,2,3]
for i in a:
    print(i)
#
# List without using variable
for i in ['a','b','c']:
    print(i)

# Tuple,Set
# for i in (1,2,3,4):
#     print(i)

# a = ('a','b','z','y')
# for i in a:
#     print(i)

# a = [1,2,3,4,5,4,3,2,1]
# for i in a:
#     print(i)
#
# for i in range(1,5):
#     print(i)
# for j in range(5,0,-1):
#     print(j)

#Table:-
# num = int(input("Enter a number: "))
# for a in range(1,11):
#     print(num, "*", a, "=", num*a)

# Sum of 10 Natural Numbers
# sum = 0
# for i in range(1,11):
#     sum = sum + i
#     print(sum)

# break is a keyword in python used to terminate the flow of a loop
# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# for i in range(1,401):
#     if i % 2 == 0 or i % 4 == 0:
#         print(i)

# for i in range(1, 401):
#     if i % 2 == 0 and i % 4 == 0:
#         print(i)


# num = int(input("Enter a Number: "))
# prime = True
# for i in range(2,num):
#     if num % i == 0:
#         prime = False
#         break
# if prime == False:
#     print(num, "is not prime")
# else:
#     print(num, "is prime")



