# Python methods (inbuilt functions) built-in functions for list, tuple, string, dict, set.

# list methods in python
# l = [1,2,3,3,4,5,5,6,7,8,9,0]
# # l.pop(1)
# m = l.copy()
# c = l.count(5)
# # l.sort()
# l.remove(2)
# l.reverse()
# # x = l.index(3,25)
# print(m)
# print(c)
# # print(x)
# # print(l)
#
# l.sort()
# d = l.insert(1,"Messi")
# x = l.index(8)
# print(l)
# print(x)
# x =[]
# l = [12,1,32,1,4,5,1,0]
# l.sort()
# l.remove(1), l.remove(1), l.remove(1)
# l.insert(5,1), l.insert(6,1), l.insert(7,1)
# print(l)


# for i in l:
#     if i == 1:
#         x.append(i)
#         l.remove(i)
# l.extend(x)
# print(l)
# g = []
# s = ['a','23','k','3','7','l']
# s.sort()
# l = s[:3]
# for i in l:
#     print(int(i))

input = [(1,'a'),(2,'b'),(3,'c')]

# output = [[1,2,3],['a','b','c']]
# numbers = []
# strings = []
# for i in input:
#     numbers.append(i[0])
#     strings.append(i[1])
#     # print(int(i))
# output = [numbers,strings]
# print(output)

# f = []
# k = []
# for i in input:
#     f.append(i[0])
#     k.append(i[1])
# print(f)
# print(k)

l = []
k = []
kl = []
for i in input[0]:
    l.append(i)
for i in input[1]:
    l.append(i)
for i in input[2]:
    l.append(i)
print(l)
for i in l:
    if type(i) == str:
        k.append(i)
    else:
        kl.append(i)
print([k]+[kl])
