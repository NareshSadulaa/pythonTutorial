x = int(input("Enter a number: "))
y = int(input("Enter a another number: "))
choice = input("Make a choice(+,-,*,/) : ")
if choice == "+":
    print(x+y)
elif choice == "-":
    print(x-y)
elif choice == "*":
    print(x*y)
elif choice == "/":
    print(x/y)
else:
    print("Invalid choice")
