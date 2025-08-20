#Constructor Method/Magical Method/Dunder Method--
#self Connections between Functions
#Syntax-
#        def __init__(self):

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a)
#         print(self.b)
#     def add(self):
#         print(self.a+self.b)
#     def Subtract(self):
#         print(self.a-self.b)
#     def Multiply(self):
#         print(self.a*self.b)
# o=A(8,7)
# o.add()
# o.Subtract()
# o.Multiply()


# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.salary)
# g=Employee("Gaurav",22,60000)
# g.show()


#Calculator

# class Calculator:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def Add(self):
#         print(self.x, "+", self.y, "=" ,self.x+self.y)
#     def Subtract(self):
#         print(self.x, "-", self.y, "=" ,self.x-self.y)
#     def Multiply(self):
#         print(self.x, "*", self.y, "=" ,self.x*self.y)
#     def Division(self):
#         print(self.x, "/", self.y, "=" ,self.x/self.y)
#
#     def Main(self):
#         intr=input("Enter the Operation :")
#         if intr=="+":
#             c.Add()
#         elif intr=="-":
#             c.Subtract()
#         elif intr=="*":
#             c.Multiply()
#         elif intr=="/":
#             c.Division()
#         else:
#             print("Invalid Operator")
# num1=int(input("Enter the Number :"))
# num2=int(input("Enter the Number :"))
# c=Calculator(num1,num2)
# c.Main()


#Signup Page

# class Signup:
#     def __init__(self,username,passw):
#         self.username=username
#         self.passw=passw
#     def Login(self):
#         print("Now Login to the Page")
#         userr=input("Enter the Username :")
#         if userr==self.username and "@" in self.username:
#             print("Username is Correct")
#             passs=input("Enter the Password :")
#             if passs==self.passw and len(self.passw)==7:
#                 print("Access Granted")
#             else:
#                 print("Invalid Password")
#         else:
#             print("Invalid Username!")
# x=input("Fix Your Username which contains @ :")
# y=input("Fix Your Password which contains 7 Character :")
# g=Signup(x,y)
# g.Login()


#4 subjects Give Total and Percentage
#
# class Marks:
#     def __init__(self,marks1,marks2,marks3,marks4):
#         self.marks1=marks1
#         self.marks2 =marks2
#         self.marks3 =marks3
#         self.marks4 =marks4
#
#     def result(self):
#         tot=input("Enter what you want Total or Percentage :")
#         if tot=="Total":
#             print(self.marks1+self.marks2+self.marks3+self.marks4)
#         elif tot=="Percentage":
#             print(((self.marks1+self.marks2+self.marks3+self.marks4)/400)*100,"%")
#
# a=int(input("Enter the marks of English :"))
# b=int(input("Enter the marks of Maths :"))
# c=int(input("Enter the marks of Science :"))
# d=int(input("Enter the marks of Drawing :"))
# m=Marks(a,b,c,d)
# m.result()