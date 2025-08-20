# user = "admin"
# passw = 1234
# user2 = input("Enter username: ")
# if user == user2:
#     pass2 = int(input("Enter password: "))
#     if pass2 == passw:
#         print("Access granted")
#     else:
#         print("Password is incorrect.....")
# else:
#     print("Check Username...")

# stud = int(input("Enter 12th marks: "))
# if stud >= 50:
#     print("Eligible for graduation")
#     graduation = int(input("Enter graduation marks: "))
#     if graduation >= 60:
#         print("Eligible for doing job")
#     else:
#         print("Not eligible for doing job")
# else:
#     print("Not eligible for graduation")

#check length of string
# a = "Messi is the Greatest Football Player of this Generation"
# print(len(a))
#
# b = ['M','E','S','S','I']
# print(len(b))

#check if a string is empty
# a = ""
# user = input("Enter a value: ")
# a += user
# if a == "" and a == user:
#     print(a, "does not contain any values")
# else:
#     print(a, "contains values")

#Finding Lenght of integers
# user = int(input("Enter a number: "))
# a = str(user)
# print(len(a))


#Swapping numbers without using third variable
# a = 2
# b = 3
# c = 4
# d = 5
# a, b, c, d = b, d, c, a
#
# print(a)
# print(b)
# print(c)
# print(d)

user = int(input("Enter a number: "))
sum = [2,3,4,5]
mon = [6,7,8,9]
win = [10,11,12,1]
if user in sum:
    print("Summer Season")
elif user in mon:
    print("Monsoon Season")
elif user in win:
    print("Winter Season")
else:
    print("Invalid")

