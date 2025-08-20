# import matplotlib.pyplot as plt
# data = ['Python','Java','Php','MySQL','.NET']
# marks = [33,45,67,89,78.5]
# plt.pie(marks,labels=data)
# plt.show()

# l = [2,3,4,1,5,6]
# m = [4,3,2,5,6,6]
# plt.scatter(l,m)
# plt.xlabel('marks')
# plt.ylabel('percentage')
# plt.show()

# data = ['Python','Java','Php','MySQL','.NET']
# marks = [3,4,5,2.5,7]
# plt.bar(data,marks)
# plt.show()

# What is Decorator?
# Decorator means to change the behavior of a function without modifying the existing function

# def outer(f):
#     def mul(v,n):
#         return v*n
#     return mul

# @outer
# def add(v,n):
#     return v + n
# print(add(23,9))

# def mess(f):
#     def square(n):
#         return n **2
#     return square
#
# @mess
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factorial(5))
#
# @mess
# def cube(n):
#     return n**3
# print(cube(5))

# def mess(f):
#     def rev(num):
#         for i in range(num,0,-1):
#             print(i)
#     return rev
# @mess
# def seq(num):
#     for i in range(1,num+1):
#         print(i)
# num = int(input('Enter a number: '))
# seq(num)

# MultiThreading:-
        # Multi-Threading is concurrent process of execution with multiple threads
        # to perform a task simultaneously

from threading import *
from time import sleep
class process1(Thread):
    def run(self):
        for i in range(1,11):
            print('hello')
            sleep(1)

class process2(Thread):
    def run(self):
        for i in range(11,21):
            print('world')
            sleep(1)

x = process1()
y = process2()
x.start()
y.start()
