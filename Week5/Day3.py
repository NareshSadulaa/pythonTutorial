# Abstraction in python
# Show essential data while hiding implementation
# To perform abstraction in python we need to import abstractmethod from abc module
# abc = abstract class method

# from abc import ABC,abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def deposit():
#         pass
#     def withdraw():
#         pass
# class ATM(Bank):
#     def deposit():
#         print("deposit")
#
# per1 = ATM
# per1.deposit()
# class Bank:
#     def __init__(self):
#         self.balance = 0
#     def show_balance(self):
#         self.balance = 0
#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += self.amount
#         self.show_balance()
#     def withdraw(self,amount):
#         self.amount = amount
#         if (self.amount > self.balance):
#             print(f"You don't have enough money")
#         else:
#             self.balance -= amount
#         self.show_balance()
#     def main(self):
#         print("Welcome to Bank")
#         print("1. View Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
#         choice = input("Enter your choice: ")
#         while(True):
#             if choice == "1":
#                 print("your current balance is: ",self.balance)
#                 obj.show_balance()
#             elif choice == "2":
#                 amount = int(input("Enter amount to deposit: "))
#                 obj.deposit(amount)
#             elif choice == "3":
#                 amount = int(input("Enter amount to withdraw: "))
#                 obj.withdraw(amount)
#             elif choice == "4":
#                 pass
#             else:
#                 print("Invalid choice")
#             break
# obj = Bank()
# obj.main()

str = "DONT talk SHOW me YOUR code"
list = str.split(" ")
m = []
for i in list:
        m.append(i)
print(m)
