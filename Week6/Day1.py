# File handling in python
# open() is a function used to open any file in the current working directory

# There are some modes to perform file handling
# r = read mode
# w = write mode : overrides the existing data.
# a = append mode : adds data to the file with existing data.

# there are also pickling and unpickling concept in file handling in which data encrypted in binary format

# There are some functions to perform this
# load = binary data convert into object
# dump = converts data into binary
# wb = write binary
# rb = read binary

# data = open('demo','r')
# print(data.read())

# data = open('demo','w')
# print(data.write('That is java'))

# data = open('demo','a')
# print(data.write('\nThis is python'))

# import pickle
# data = {"user":"admin","password":1234}
# file = open('xyz.cbc','wb')
# b = pickle.dump(data,file)

# file = open('xyz.cbc','rb')
# r = pickle.load(file)
# print(r)

# data = {
#     "Binary data is data that’s represented using only 0s and 1s — the language of computers. Every file, photo, video, or code you use on a computer or mobile is ultimately stored and processed in binary form."
# }
# file = open('data.bkl','wb')
# pickle.dump(data, file)

# file = open('Data.pickle','rb')
# r = pickle.load(file)
# print(r)

# while True:
#     ch = int(input("Enter a number: "))
#     if ch == 1:
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         location = input("Enter your location: ")
#         data = open('demo','w')
#         data.write(name + "\n")
#         data.write(age+' \n')
#         data.write((location + '\n'))
#     elif ch == 2:
#         data = open('demo','r')
#         print(data.read())
#     else:
#         print("Enter a valid choice")

while True:
    ch = int(input("Enter a number: "))
    if ch == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        add = num1 + num2
        data = open('demo','w')
        print(data.write(str(add) + "\n"))
    elif ch == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        sub = num1 - num2
        data = open('demo','a')
        print()
        print(data.write(str(sub) + "\n"))
    elif ch == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        mul = num1 * num2
        data = open('demo','a')
        print(data.write(str(mul) + "\n"))
    elif ch == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        div = num1 / num2
        data = open('demo','a')
        print(data.write(str(div) + "\n"))
    elif ch == 5:
        data = open('demo','r')
        print(data.read())
    else:
        print("Invalid input")