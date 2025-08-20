#Inheritance in Python--
#Inheritance means the child/sub/derived Class access the properties of the
#Parental/Super Class
#Types of Inheritance
#1)Single Level Inheritance
#2)Multi Level Inheritance
#3)Multiple Inheritance
#4)Hierarchical Inheritance


# Single Inheritance
# One child/ Sub class inherit the properties of one parent/Super class
# class A:
#     def show():
#         print("I am a python developer.")
#     def show1():
#         print("I am a java developer.")
# class B(A):
#     def show2():
#         print("I am a php developer.")
#     def show3():
#         print("I am a frontend developer.")
# p1 = B
# p1.show3()

# class A:
#     def __init__(self):
#         self.x = 5
#
#     def square(self):
#         print(self.x ** 2)
# class B(A):
#     def __init__(self):
#         self.y = 4
#         A.__init__(self)
#     def add(self):
#         print(self.x + self.y)
# O = B
# O.add()

# class A:
#     def __init(self):
#         self.x = 5
#     def square(self):
#         self.x **= 2
# class B(A):
#     def __init__(self):
#         self.y = 4
#         A.show(self)
#
#     def show2(self):
#         print(self.x + self.y)
# o = B
# o.show()

# class phone:
#     def calling():
#         print("This is a call log")
#     def messages():
#         print("This is a message log")
# class smartphone(phone):
#     def gaming():
#         print("This is phone has a gaming support")
#     def camera():
#         print("This is phone has a camera support")
# # ft = phone
# # ft.calling()
# cell = smartphone
# cell.calling()

# class phone:
#     def __init__(self):
#         self.call= "Calling"
#         self.mess= "Messages"
#     def show(self):
#         print(f'phone having {self.call} and {self.mess}')
# class smartphone(phone):
#     def __init__(self):
#         self.camera= "Camera"
#         self.games = "Games"
#         phone.__init__(self)
#     def show2(self):
#         print(f'Smartphone having {self.camera} and {self.games}')
# model = smartphone()
# model.show2()

# class maruti:
#     def __init__(self):
#         self.f1 = "Petrol"
#     def show(self):
#         print(f"Maruti having {self.f1}")
# class swift(maruti):
#     def __init__(self):
#         self.f2 = "Diesel"
#         maruti.__init__(self)
#     def show1(self):
#         print(f"Swift having {self.f2}")
# class nexon(swift):
#     def __init__(self):
#         self.f3 = "Electric"
#         maruti.__init__(self)
#         swift.__init__(self)
#     def show2(self):
#         print(f"Nexon having {self.f3}")
#
# car = nexon()
# car.show2()

# class square:
#     def __init__(self):
#         self.x = 5
#         self.squ = self.x**2
#     # def show(self):
#     #     return self.squ
# class rectangle(square):
#     def __init__(self):
#         self.l = 10
#         self.y = 2
#         self.rect = self.l * self.y
#         square.__init__(self)
#     # def show(self):
#     #     return self.rect
# class show(rectangle):
#     def square(self):
#         print(f"The Area of Square is {self.squ}")
#         rectangle.__init__(self)
#     def rectangle(self):
#         print(f"The Area of Rectangle is {self.rect}")
#
# Area = show()
# Area.square()
# Area.rectangle()
