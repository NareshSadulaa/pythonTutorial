import re
class Webshopping:
    def _init_(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "SS":
            print("Login successful")
        elif password == "11":
            print("Login successful pass correctly")
        else:
            print("Login failed")
        self.username = username
    def show_products(self):
        print("\nHere are the products available:\n")
        self.products = {
            "Laptop": 12000,
            "Smartphone": 8000,
            "Headphones": 300,
            "T-shirt": 250,
            "Ring": 12000,
            "Sneakers": 750
        }
        for item in self.products:
            print(item, "-", self.products[item])
    def buy_product(self):
        self.selected_product = input("\nEnter the name of the product you want to buy: ")
        if self.selected_product in self.products:
            print(f"{self.selected_product} is available.")
            self.price_to_pay = self.products[self.selected_product]
            print("Price:", self.price_to_pay)
        else:
            print("Product not found.")
            self.buy_product()
    def payment(self):
        print("\nPayment Options:\n1.Credit Card\n2.Google Pay\n3.Paytm\n4.Net Banking")
        choice = input("Enter your payment option (1/2/3/4): ")
        if choice == "1":
            cc = input("Enter credit card number: ")
            if len(cc) == 16 and cc.isnumeric():
                cvv = input("Enter CVV: ")
                if len(cvv) == 3 and cvv.isnumeric():
                    print("Payment successful using Credit Card.")
                else:
                    print("Invalid CVV.")
            else:
                print("Invalid credit card number.")
        elif choice == "2":
            gpay = input("Enter Google Pay number: ")
            if len(gpay) == 10 and gpay.isnumeric():
                utr = input("Enter UTR number: ")
                if len(utr) == 10 and utr.isnumeric():
                    print("Payment successful using Google Pay.")
                else:
                    print("Invalid UTR number.")
            else:
                print("Invalid Google Pay number.")
        elif choice == "3":
            paytm = input("Enter Paytm number: ")
            if len(paytm) == 10 and paytm.isnumeric():
                utr = input("Enter UTR number: ")
                if len(utr) == 10 and utr.isnumeric():
                    print("Payment successful using Paytm.")
                else:
                    print("Invalid UTR number.")
            else:
                print("Invalid Paytm number.")
        elif choice == "4":
            account_no = input("Enter Account Number: ")
            if len(account_no) == 14 and account_no.isnumeric():
                ifsc = input("Enter IFSC Code: ")
                if re.match("^[A-Z]{4}0[A-Z0-9]{6}$", ifsc):
                    print("Payment successful using Net Banking.")
                else:
                    print("Invalid IFSC code.")
            else:
                print("Invalid Account Number.")
        else:
            print("Invalid payment option.")

webshop = Webshopping()
webshop.show_products()
webshop.buy_product()
webshop.payment()
