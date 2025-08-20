# functions in python
# functions in python are block of code only runs when we call it
#
# in python there are four types of functions
# 1) inbuilt functions
# 2) user-defined functions
# 3) lambda functions
# 4) recursive functions
#
# how we can create user-defined functions
# syntax:-
# def function_name():
#     Block of a Code

# Printing Tables Using functions
# def table():
#     user= int(input("Enter a number: "))
#     for i in range(1, 11):
#         print(user, "*", i, "=", user * i)
#     print()
#
# table()
# table()
# table()

# Prime Numbers
# def prime():
#     num = int(input("Enter a number: "))
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#
#     if (prime == False):
#         print("The number is not a prime number")
#     else:
#         print("The number is a prime number")
#
# prime()

# Printing Even and Odd Numbers using functions
# def EvnOdd():
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# EvnOdd()


# User-defined functions
# 1) functions without parameters
# 2) functions with parameter
# 3) variable length arguments
# 4) default variable
# 5) keyword arguments


# Syntax for functions with parameters
# def gunc_name(parameters):
#     Block of code
#
# gunc_name(arguments)

# Printing Factorial of a number using Parameter function
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#         print(fact,end=" ")
# factorial(0)


# return keyword
# return is a keyword in python which is used to store the data/output into the function

# def f():
#     a = 34
#     b = 3
#     c = a*b
#     return c, a + b + c, a/b, a%b, a**b, a//b**b, a == b, a>=b
#
# print(f())

# continue: Continue is a keyword in python to skip the current position in the code/loop

# for i in range(1,10):
#     if i == 2:
#         continue
#     print(i)


# Pass: pass is a keyword in python to skip the particular code/loops which we left half-written
# Example:-
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         pass

def person():
    print("A person is walking....")
    for i in range(5):
        if i == 3:
            user = input("Are you tired?  ")
            if user == "y" or user == "yes" or user == "YES" or user == "Y":
                print("Take Rest..")
                break
            else:
                print("Okiee, then continue Walking")
        else:
            continue
person()