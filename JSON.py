# import json

# x = '{"name" : "naresh", "age" : 22, "address" : "Barcelona", "country": "spain" }'
#
# y = json.loads(x)
#
# print(y['age'])

# x = {
#     'name': 'naresh',
#     'age': 22,
#     'relationships': None,
#     'email': 'sadulanaresh22@gmail.com',
#     'country': 'India'
# }
# y = json.dumps(x)
# print(y)

# num = int(input("Enter a number: "))
# if num < 0:
#     raise Exception("Sorry no numbers below 0")
# else:
#     for i in range(1,11):
#         print(num,"x",i,'=',num*i)
#
#

import time

a = []
current_time = time.time()
for i in range(1,101):
    a.append(i)
print(a)
final_time = time.time()-current_time
print(final_time)

y = [a for a in range(1,101)]
print(y)
