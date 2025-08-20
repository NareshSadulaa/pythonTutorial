# Control flow in Python
# 1) Conditional Statements
# 2) loops
#
# 1) Conditional Statements
# if, if-else, if-elif-else, nested-if
#
# Syntax:-
# 1) if (condition):
#     statements
#
# 2) if (condition):
#         statements
#    else:
#        statements
#
# 3) if (condition):
#     statements
#    elif (condition):
#        statements
#    else:
#        statements
#
# 4)
# if (condition):
#     statements
#     if(condition):
#         statements
#     else:
#         statements
# else:
#     statements

#
# num = int(input("Enter a number: "))
#
# if (num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")
#
#
# person = int(input("Enter a person: "))
# if (person >= 18):
#     print("You are eligible")
# else:
#     print("You are not eligible")

# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive", num)
# elif num == 0:
#     print("The number is zero")
# else:
#     print("The number is negative", num)

# l = [1,2,3,4,5]
# num = int(input("Enter a number: "))
# if num not in l:
#     print("The Number is absent in the list")
# else:
#     print("The Number is present in the list")


# x = int(input("Enter a number: "))
# y = int(input("Enter a another number: "))
# if x > y:
#     print('The number is' ,x ,'greater than',y)
# elif x < y:
#     print('The number is' ,x ,'less than',y)
# else:
#     print('The number is' ,x ,'equals',y)\

x = int(input("Enter a number: "))
y = int(input("Enter a another number: "))
choice = input("Make a choice(+,-,*,/) : ")
if choice == "+":
    print(x+y)
elif choice == "-":
    print(x-y)
elif choice == "*":
    print(x*y)
elif choice == "/":
    if y == 0:
        print("Invalid input")
    else:
        print(x/y)
else:
    print("Invalid choice")