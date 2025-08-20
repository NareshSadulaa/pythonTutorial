# class Stack:
#     def __init__(self):
#         self.i = []
#     def insert(self,a):
#         self.i.append(a)
#         print(self.i)
#     def remove(self):
#         self.i.pop()
#         print(self.i)
#
#     def main(self):
#         while True:
#             ch = int(input("Enter your choice: "))
#             if ch == 1:
#                 b = int(input("Enter the element: "))
#                 self.insert(b)
#             elif ch == 2:
#                 self.remove()
#             elif ch == 3:
#                 break
#             else:
#                 print("Please enter a valid choice")
#
# obj = Stack()
# obj.main()

# class Queue:
#     def __init__(self):
#         self.q = []
#     def insert(self, a):
#         self.q.append(a)
#         print(self.q)
#     def remove(self):
#         self.q.pop(0)
#         print(self.q)
#     def main(self):
#         while True:
#             ch = int(input("enter your choice: "))
#             if ch == 1:
#                 b = int(input("enter the element: "))
#                 self.insert(b)
#             elif ch == 2:
#                 self.remove()
#             elif ch == 3:
#                 break
#             else:
#                 print("Please enter a valid choice.")
#
# obj = Queue()
# obj.main()

# l = [12,3,4,67,99,73,76]
#
# for i in range(len(l)):
#     for j in range(len(l)-i-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)

