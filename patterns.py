# # Right-Half Pyramid
# x = 5
# for i in range(1, x + 1):
#     for j in range(1, i):
#         print("*", end=" ")
#     print()
# print()
# # Inverted Right-Half Pyramid
# m = 5
# for i in range(1, m + 1):
#     for j in range(5, i, -1):
#         print("*", end=" ")
#     print()

# # Left-Half Pyramid
# y = 5
# for i in range(1, y + 1):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for k in range(i, 1, -1):
#         print("*", end=" ")
#     print()
# print()

# #Left-Half Inverted Pyramid
# r = 5
# for i in range(r, 1, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for k in range(i, 1, -1):
#         print("*", end=" ")
#     print()

# # Pyramid
# u = 5
# for i in range(1, u + 1):
#     for j in range(i, 5):
#         print(end=" ")
#     for k in range(i, 1, -1):
#         print('*', end=" ")
#     print()
# print()
# #Inverted Pyramid
# o = 5
# for i in range(o, 1, -1):
#     for j in range(5, i, -1):
#         print("", end=" ")
#     for k in range(i, 1, -1):
#         print(i, end=" ")
#     print()

# #Diamond Pattern
# t = 5
# for i in range(1, t + 1):
#     for j in range(i, 5):
#         print(end=" ")
#     for k in range(i, 1, -1):
#         print("*", end=" ")
#     print()
# for i in range(t, 1, -1):
#     for j in range(5, i, -1):
#         print("", end=" ")
#     for k in range(i, 1, -1):
#         print("*", end=" ")
#     print()

# #Numbers Pattern
# l = 5
# for i in range(l):
#     i += 1
#     for j in range(i, 5):
#         print(end=" ")
#     for k in range(i, 0, -1):
#         print(i, end=" ")
#     print()
# print()

x = lambda a : a + 1
print(x(1))
