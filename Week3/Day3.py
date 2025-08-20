# Lambda Function in Python
#     lambda is a keyword in python by which we can create single functions:
# But lambda function can perform only operation at a time
# if we want to perform multiple operations we have to use more/multiple lambda functions

# add = lambda e,f:e+f
# sub = lambda e,f:e-f
# mul = lambda e,f:e*f
# div = lambda e,f:f/e
# print(add(5,9),sub(5,9),mul(0,4),div(5,4))

# num = int(input("Enter a Number: "))
# num2 = lambda num: num * num
# print(num2(num))

# lambda function with condition
# o = lambda x,y:print("x is greater than y")if x>y else("y is greater than x")
# print(o(1,2))

# o = lambda x:print("x is a negative number")if x<0 else("x is a positive number")
# o(-1)

# Powerful functions in python
# # Map, Filter, Reduce
# 1) Map : map function perform operation on each element in list/tuple
#    Syntax : object = map(functions,iterator)
# 2) Filter : filter is used to FilterOut the elemengt according to the condition
#      Syntax : object = filter(functions,iterator)
# 3) Reduce : reduce returns single value as per operation

# Map
l = [1,2,3,4,5,6,7,8,9]
# square = map(lambda x: x**2,l)
# print(list(square))
#
# fil = filter(lambda x:x%2==0,l)
# print(list(fil))

# print("Enter your name: ")
# name = input()
# print(f"Hello {name}")

# Filter
# x = [2,'python',3,'java',4,'php']
# mul = filter(lambda x:x==str(x),x)
# print(list(mul))

# Reduce
from functools import reduce
# a = [1,2,3,4,5,6]
add = reduce(lambda x,y:x+y,l)
print(add)

# s = [1,-4,5,-6,-7,8,10,-1]
# a = filter(lambda x:x>0,s)
# add2 = reduce(lambda x,y:x+y,a)
# print(add2)

strings = ['python','java','php','kotlin','c++','c','c#','Go']
a = filter(lambda a: len(a) == 3,strings )
print(list(a))
