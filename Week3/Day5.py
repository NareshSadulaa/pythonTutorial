# Tuple methods in Python
# In Python, Lists are mutable which means that they can be modified
# But Tuples are immutable which means that they cannot be modified once it has been declared

# t = (1,2,3,4,5,6,7,3,4,5)
# s = t.count(3)
# f = t.index(6)
# print(s)
# print(f)

# list Comprehension
# This is a list method which is only applicable/used with lists not any other sequential types

# obj = [variable for variable in range()] = Syntax

# x = [i for i in range(1,11)]
# print(x)

# y = [a for a in range(1,1001) if a % 2 == 0]
# print(y, end=" ")

# user = int(input("Enter a number: "))
# x = [user * i for i in range(1,11) ]
# print(x)


# d = {'name':'Messi','age':18,1:25,2:53,3:61}
# d.pop('age')
# d.popitem()
# d.update({'age':18})
# m = d.values()
# x = d.items()
# n = d.get('name')
# k = d.keys()
# print(d)
# print(m)
# print(x)
# print(n)
# print(k)

data = {'even':[2,4,6,8,10],'odd':[1,3,5,7,9]}
# for i in data['even']:
#     print(i)
# print(data['odd'])
for i in data:
    print(i)
choice = int(input('Enter your choice(1/2): '))
if choice == 1:
    for i in data['even']:
        print(i)
elif choice == 2:
    for i in data['odd']:
        print(i)
else:
    print('Invalid choice')