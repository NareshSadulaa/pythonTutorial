# Methods of Sets in Python
from time import perf_counter_ns

import unzip
from langchain.chains.constitutional_ai.principles import PRINCIPLES


# a = {1,2,3,4,5,6,7}
# b = {7,8,9,4,3,2,1}

# h = print(a.copy())
# i = print(a.pop())
# a.update({8,9,10})
# a.remove(8)
# a.clear()
# print(a)

# x = a.union(b)
# y = b.intersection(a)
# print(x)
# print(y)
# print(a.add(18),a)
# print(a.difference(b))

# a.discard(18)
# # print(a)
# a.remove(1)
# print(a)


# List's Zip and Unzip methods
# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11,12]
# z = list(zip(a,b,c))
# # print(z)
#
# a,b,c  = zip(*z)
# print(a,b,c)

# Example of while True
# passw = 1234
# while True:
#     num = int(input("Enter a number: "))
#     if num == passw:
#         print("Password matched")
#         break
#     print("Wrong Password")


# passw = 1234
# inp = int(input("Enter Password: "))
# while True:
#     if inp != passw:
#         print("You have 3 chance to enter correct password")
#         inp = int(input("Enter Password: "))
#         if inp != passw:
#             print("You have 2 chance to enter correct password")
#             inp = int(input("Enter Password: "))
#             if inp != passw:
#                 print("You have 1 chance to enter correct password")
#                 inp = int(input("Enter Password: "))
#             else:
#                 print("Access Granted")
#                 continue
#         else:
#             print("Access granted")
#             continue
#     else:
#         print("Access granted")
#         continue
#
#     print("Account Blocked")
#     break
#
# if passw == inp:
#     print("Access granted")
# else:
#     print("you have 3 chances to enter correct password")
#     for i in range(1,4):
#         inp = int(input("Enter Password: "))
#         if passw == inp:
#             print("Access granted")
#             break
#         else:
#             continue
#     print("Account Blocked")



# a = (1)
# print(type(a))
# b = 1,
# print(type(b))

#
# def person():
#     print("A person is walking....")
#     for i in range(5):
#         if i == 3:
#             user = input("Are you tired?  ")
#             if user == "y" :
#                 print("Take Rest..")
#                 break
#             else:
#                 print("Okiee, then continue Walking")
#         else:
#             continue
# person()

def person():
    print("A person is running...")
    while True:
        for i in range(1,6):
            if i == 1:
                user = input("Are you tired?")
                if user == 'y':
                    print("take rest")
                    break
            elif i == 2:
                user = input("Are you tired?")
                if user == 'y':
                    print("take rest")
                    break
            elif i == 3:
                user = input("Are you tired?")
                if user == 'y':
                    print("take rest")
                    break
            elif i == 4:
                user = input("Are you tired?")
                if user == 'y':
                    print("take rest")
                    break
            else:
                print("Congratulations, you won...")
        break



person()