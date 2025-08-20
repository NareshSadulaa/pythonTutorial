# Object-Oriented Programming (oop's)
# oops in programming is real world way to achieve programming task by oop's

# Concepts in Oops
# class
# object
# inheritance
# polymorphism
# encapsulation
# abstraction

# What is Class?
# Class is a blueprint of object and also the collection of methods

# What is Object?
# Object is the representative of class, in python everything is an object

# class Calculator:
#     def add(a,b):
#         print(a+b)
#     def sub(a,b):
#         print(a-b)
#     def mul(a,b):
#         print(a*b)
#     def div(a,b):
#         print(a/b)
#     def table(a):
#         for i in range(1,11):
#             print(a,"*",i,"=",a*i)
#     def factorial(n):
#         sum = 1
#         for i in range(1,n+1):
#             sum *= i
#             print(sum)
#
# camel = Calculator
# camel.factorial(5)

# class Person:
#     def show(name, age,location):
#         print(f"My name is {name},i am {age}years old,i stay at {location}")
#
# x = input("Enter your name: ")
# y = int(input("Enter your age: "))
# z = input("Enter your location: ")
# p1 = Person
# p1.show(x,y,z)
#
#


class Validation:
    def show(self,email,password):
        if  '@' in email:
            s = str(password).isalnum()
            if len(y) == 8 and y.capitalize() and y.isalnum():
                print('Registered Successfully')
            else:
                print('Password should be at least 8 characters long')
        else:
            print('Email should contain @.')


z = Validation()
x = input("Enter email-id: ")
y = input('Enter your password: ')
z.show(x,y)

