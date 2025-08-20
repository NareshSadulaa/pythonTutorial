# l = [1,2,3,'a','b','c']
# for i in l:
#     if type(i) == str:
#         print(i)

# num = 145
# num1 = str(num)
# sum = 0
# for i in num1:
#     sum += int(i)
# print(sum)


# num = list('1','4','5')
# for i in (num):
#     num = int(i)
#     print(type(num))


# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print(i,end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for j in range(i):
#         print(i,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(i):
#         if i == 1:
#             print('@', end=" ")
#         if i == 2:
#             print('$', end=" ")
#         if i == 3:
#             print('!', end=" ")
#         if i == 4:
#             print('^', end=" ")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# for i in range(1,5):
#     for j in range(5,i,-1):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# x = [1,2,3,4]
# y = [5,6,7,1]
# for i in x:
#     for j in y:
#         if i == j:
#             print(i)

# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(i,end=" ")
#     print()


num = int(input("Enter a number: "))
len = str(num)
for i in len:
    sum = int(len)
    sum2 = num ** sum
    print(sum2)


