# k = []
# l = [1,-2,3,-4,5,-6]
# m =[]
# for i in l:
#     if i < 0:
#         k.append(i)
#     else:
#         m.append(i)
# print(k)
# print(m)

# k = []
# l = [1,2,3,'a','b','c']
# m = []
# for i in l:
#     if type(i) is str:
#         m.append(i)
#     else:
#         k.append(i)
# print(m)
# print(k)

# k=[]
# l = []
# for i in range(1,100):
#     if i % 2 == 0:
#         l.append(i)
#     else:
#         k.append(i)
# print("Even Numbers: ",l)
# print("Odd Numbers: ",k)

# l = []
# size = int(input("Enter the size of list: "))
# for i in range(0,size):
#     ele = int(input("Enter the element: "))
#     l.append(ele)
#
# print(l)

# p= []
# for i in range(1,11):
#     ele = int(input("Enter elements : "))
#     if ele<0:
#         break;
#     else:
#         p.append(ele)
# print(p)


# l = [2,5,6,7,8]
# m = [1,3,6,2,9]
# for i in m:
#     l.append(i)
# k = set(l)
# n = list(k)
# print(n)

# l = [2,5,6,7,8]
# m = [1,3,6,2,9]
# for i in m:
#     if i not in l:
#         l.append(i)
#
# print(l)

l = [1,2,3,4,5]
m = [6,7,8,9,10]
m.extend(l)
print(m)