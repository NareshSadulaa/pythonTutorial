# num = int(input("Enter a number: "))
# num2 = str(num)
# power = len(num2)
# sum = 0
# for i in num2:
#     sum = sum + int(i) ** power
# if num == sum:
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")


# a = 4
# b = 5
# [a, b + 1] = b, a + 1
# print(a)

# k = 'Python'
# print(k[1:3])
# print(k[-5:-2])
#
# m = [1,2,3,4,4]
# print(m[::3])

# a = 'HELLO, WORLD'
# print(a.strip())

# rev = ''
# a = 'python'
# for i in a:
#     rev = i + rev
# print(rev)

# user = input("Enter a String: ")
# i = len(user)-1
# index = int(input("Enter a index: "))
# if i >= index:
#     print(user[index])
# else:
#     print("Not Found")
#
# k = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# # print(k[2][1:])
#
# for i in k[0]:
#     print(i)


p = [[1,-2,3],[-4,5,-6]]
l = []
m = []
for i in p[0]:
    if i > 0:
        l.append(i)
    else:
        m.append(i)
for i in p[1]:
    if i < 0:
        m.append(i)
    else:
        l.append(i)
print(l)
print(m)


# p = [[1,-2,3],[-4,5,-6]]
# l = []
# m = []
# a = []
# for i in p[0]:
#     a.append(i)
# for j in p[1]:
#     a.append(j)
# for k in a:
#     if k > 0:
#         m.append(k)
#     else:
#         l.append(k)
# print(m)
# print(l)

