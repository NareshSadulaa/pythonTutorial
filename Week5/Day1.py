# Multiple Inheritance
# Two Parent and One Child
# means Two Super Classes and One Sub Class

# class num1:
#     def __init__(self):
#         self.num1 = int(input("Enter the first number: "))
# class num2:
#     def __init__(self):
#         self.num2 = int(input("Enter the second number: "))
# class Add(num1, num2):
#     def __init__(self):
#         num1.__init__(self)
#         num2.__init__(self)
#     def show(self):
#         print(f"The addition of {self.num1} and {self.num2} is {self.num1 + self.num2}")
# Op1 = Add()
# Op1.show()
#
#
# class Google:
#     def __init__(self):
#         self.map ="maps"
#     def show(self):
#         print(f"Google has {self.map}")
# class Canon:
#     def __init__(self):
#         self.camera = "Camera"
#     def show(self):
#         print(f"Canon has a {self.camera}")
# class Mobile(Google, Canon):
#     def __init__(self):
#         Google.__init__(self)
#         Canon.__init__(self)
#     def show(self):
#         print(f"Mobile Phone consists of features {self.camera} and {self.map}")
# Op1 = Mobile()
# Op1.show()

# Hierarchical Inheritance
# One Parent and Two Child
# meaning One super Class and Two sub class
#
# class Number:
#     def __init__(self):
#         self.num = int(input("Enter a Number: "))
#     def table(self):
#         for i in range(1, 11):
#             print(self.num*i)
# class Factorial:
#     def __init__(self):
#         Number.__init__(self)
#         fact = 1
#         for i in range(1,self.num+1):
#             fact *= i
#             print(fact)
# class Circle:
#     def __init__(self):
#         Number.__init__(self)
#         print(f"The Area of Circle is {3.14*self.num**2}")
# obm = Number()
# obm.table()
# obs = Circle()
# obj = Factorial()



# Polymorphism
# What is polymorphism
# One Object has many functions/methods/forms
# There are two types of Polymorphism
# 1) Method Overloading:
#     Functions having different number of arguments
#     it doesn't supported in python

# 2) Method Over-riding
#     Same function name having different functionalities

# class CAR:
#     def __init__(self):
#         self.brand = 'Toyata'
#         self.feature = 'Mapping'
#     def show(self):
#         print(f"Car is {self.brand} and has a feature {self.feature}")
# class Truck(CAR):
#     def __init__(self):
#         CAR.__init__(self)
#     def show(self):
#         print(f"Truck is {self.brand} and has a feature {self.feature}")
#
# obj = Truck()
# obj.show()



class A:
    def check(*args):
        if len(args) == 0:
            print("Empty argument")
        elif len(args) == 1:
             for i in args:
                 print(i**2)
        elif len(args) == 2:
            sum = 0
            for i in args:
                sum += i
            print(sum)

obj = A
obj.check(2,3)