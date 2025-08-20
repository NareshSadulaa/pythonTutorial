# class Calci:
#     def add():
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         print(a + b)
#     def sub():
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         print(a - b)
#     def mul():
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         print(a * b)
#     def div():
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         if b == 0:
#             print("Number cannot be divided by zero")
#         else:
#             print(a / b)


# class Details:
#     def namedetails(name,roll,marks):
#         name = input("Enter your name: ")
#         roll = int(input("Enter your roll: "))
#         marks = int(input("Enter your marks: "))
#         percent = print(marks/500*100)
#         print(f"{name} my roll number is {roll}, my marks are {marks} and i got {percent} percentage.")

# fo = 4.100799560546875e-05
# wh = 5.221366882324219e-05
# print(wh-fo)
# import time
# # l = []
# # t = time.time()
# # i = 0
# # while (i<100):
# #     i+=1
# #     l.append(i)
# # print(l)
# # final_time = time.time()-t
# # print(final_time)
#
# local = time.localtime()
# print(local.tm_hour,local.tm_min,local.tm_sec)


# import math
# num = int(input("Enter a number: "))
# # if num.reminder == 0:
# #     print("The entered number is even",num)
# # else:
# #     print("The entered number is odd",num)
# print(math.remainder(num))

# import random
# num = random.randint(1, 100)
# while True:
#     try:
#         guess = int(input('Guess a number between 1 and 100: '))
#         if guess > num:
#             print(f'Too High')
#         elif guess < num:
#             print(f'Too Low')
#         else:
#             print(f'You guessed the number correctly {num}')
#             break
#     except ValueError:
#         print('You did not enter a number.')


# import random
# num = random.randint(1,100)
# while True:
#     try:
#         guess = int(input('Guess a number between 1 and 100: '))
#         if guess < num:
#             print('Too low.')
#         elif guess > num:
#             print('Too high.')
#         else:
#             print('You guessed the number correctly.')
#             break
#     except ValueError:
#         print('You did not enter a number.')


# num = int(input('Enter a number: '))
# if num == 0:
#     pass
# elif num < 0:
#     print('You entered a negative number.')
# else:
#     # for i in range(1,11):
#     #     table = num * i
#     #     print(table)
#     i = 1
#     while i < 11:
#

# import random
#
# a = []
# username = input("Enter username: ")
# mobile = input("Enter mobile number: ")
# for i in username, mobile:
#     a.append(i)
#
#
# def otp():
#     OTP = ''
#     for i in range(2):
#         f = i == str(a).isalpha()
#         OTP += a[i]
#         i.random.choice(OTP)
#
#
# otp()


# num = int(input("Enter a number: "))
# if num == 0:
#     print("Zero")
# else:
#     i = 1
#     while i <= 10:
#         table = num * i
#         print(table)
#         i = i + 1
