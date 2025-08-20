table = int(input("Enter a Number: "))
prime = True
for i in range(2,table):
    if table % i == 0:
       prime = False

if (prime == False):
    print("The number is not a prime number")
else:
    print("The number is a prime number")
    


