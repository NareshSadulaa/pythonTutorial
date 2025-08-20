#Default Variable Functions....
# def func(a,b):
#     print("a=",a)
#     print("b=",b)
# func(b=1,a=6)
#
# def f(a=2):
#     print("a=",a)
# f(a=0)
#
# def fy():
#     # noinspection PyGlobalUndefined....
#     global x
#     x = 1
# fy()
# print(x)

#Variable length arguments....
# def f2(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)
# f2(1,2,2,4,5,6,7,8,8,9,0,7,8,7,6,65,4,43,32,)

# def func1(*args):
#     l = []
#     m = []
#     for i in args:
#         if i < 0:
#             m.append(i)
#         else:
#             l.append(i)
#     print(l)
#     print(m)
# func1(1,-2,3,-4,5,-6,7,-8)


# def func2(*args):
#     for i in args:
#         l = []
#         m = []
#
#     print(l)
#     print(m)
# func2(1,-2,3,-4,5,-6,7,-8)


# Recursive Function in python means the function which calls itself again and again
# sum = 0
# def s1():
#     global sum
#     sum +=1
#     print(sum)
#     s1()
# s1()

# Global Keyword in python helps us to modify the global variable inside a function
# i = 1
# def s2(a):
#     global i
#     i +=1
#     print(a + i)
# s2(23)

# def s3(a):
#     print(a)
#     s3(a-1)
# s3(1000)

user = int(input('Enter a number: '))
def fact():
    factorial = 1
    for i in range(1,user+1):
        factorial = factorial * i
        print(factorial)
fact()

# def s4(a):
#     if a < 1:
#         return 1
#     else:
#         return a * s4(a-1)
# print(s4(3))
