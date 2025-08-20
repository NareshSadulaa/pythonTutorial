import random
import datetime
class Panel:
    def __init__(self):
        self.product = {}
        self.f = []
    def products(self):
        self.product = {
            'electronics': {
                'Mobile': {
                    'Oppo Phone': 17999,
                    'Vivo Phone': 15899,
                    'Moto-Rola Phone': 13990,
                    'iPhone': 85000,
                    'RealMe Phone': 45000,
                    'OnePlus Phone': 35000
                },
                'Laptops': {
                    'Macbook': 129999,
                    'Lenovo': 55000,
                    'Hp': 60000,
                    'Acer': 45000,
                    'Asus': 80000,
                    'Dell': 65000
                },
                'Headphones': {
                    'Boat': 1200,
                    'Apple': 4500,
                    'RealMe': 3000,
                    'OnePlus': 1500
                }
            },
            'stationary': {
                'Writing': {
                    'Pencil Box': 100,
                    'Drawing Pencils': 200,
                    'Eraser Box': 50,
                    'Sharpener Box': 60,
                    'Ball Pen': 60,
                    'Gel Pen': 50,
                    'Black Pen': 70,
                    'Red Pen': 40
                },
                'Books': {
                    'Classmate': 45,
                    'Sundaram': 40,
                    'Regal': 45,
                    'Doms': 35
                }
            },
            'Machines': {
                'Washing Machines': {
                    'Whirlpool': 21000,
                    'Samsung': 25999,
                    'Lloyd': 12599,
                    'Haier': 15999
                },
                'Fridge': {
                    'LG': 25999,
                    'Samsung': 31999,
                    'Haier': 35999,
                    'Whirlpool': 37999
                },
                'TV': {
                    'MI': 14500,
                    'Acer': 15500,
                    'LG': 34000,
                    'Samsung': 43000
                }
            }
        }
    def display_products(self):
        self.products()
        for n in self.product:
            print(n)
        i = input('Enter Category name: ')
        if i in self.product.keys():
            print('There is a sub-category in this category which are:')
            for n in self.product[i]:
                print(n)
            k = input('Enter the product category: ')
            if k in self.product[i]:
                print('The products in this category are:')
                for i in self.product[i][k].items():
                    print(f'{i[0]}: {i[1]}')
            else:
                print('The product is not available')
        else:
            print(f'There is no such category,{i}.')
    def buy_products(self):
        while True:
            self.products()
            for n in self.product:
                print(n)
            i = input('Enter Category name: ')
            if i in self.product.keys():
                print('The products in this category are:')
                for n in self.product[i]:
                    print(n)
                k = input('Enter the product category: ')
                if k in self.product[i]:
                    print('The products in this category are:')
                    for m in self.product[i][k].items():
                        print(f'{m[0]}: {m[1]}')
                    self.buy = input('Enter the name of the product you want to buy?: ')
                    if self.buy in self.product[i][k]:
                        price = self.product[i][k][self.buy]
                        print(f"{self.buy} is available and it's cost is {price}")
                        print('Choice payment options:\n1.Credit card\n2.Google Pay\n3.Paytm\n4.Net Banking\n5.Exit')
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            self.credit_card()
                            break
                        elif choice == 2:
                            self.google_pay()
                            break
                        elif choice == 3:
                            self.paytm()
                            break
                        elif choice == 4:
                            self.netBanking()
                        elif choice == 5:
                            break
                        else:
                            print('Invalid choice')
                    else:
                        print('The product is not available')
                else:
                    print('The product is not available')
            else:
                print('Invalid Category')
    def credit_card(self):
        while True:
            credit_card = input('Enter credit card number: ')
            if len(credit_card) == 16:
                cvv = input('Enter your CVV: ')
                if len(cvv) == 3:
                    print(f"The payment for the {self.buy} has been done successfully")
                    self.f.append((self.buy,self.get_price()))
                    break
                else:
                    print('Invalid CVV')
            else:
                print('Invalid Credit card number')
    def google_pay(self):
        while True:
            upi = input('Enter your upi number: ')
            if len(upi) == 10:
                pin = input('Enter your pin: ')
                if pin == '1108':
                    print(f"The payment for the {self.buy} has been done successfully")
                    self.f.append((self.buy,self.get_price()))
                    break
                else:
                    print('Invalid Pin')
            else:
                print('Invalid upi number')
    def paytm(self):
        while True:
            paytm_number = input('Enter your paytm number: ')
            if len(paytm_number) == 10:
                paytm_pin = input('Enter your paytm pin: ')
                if paytm_pin == '1108':
                    print(f"The payment for the {self.buy} has been done successfully")
                    self.f.append((self.buy,self.get_price()))
                    break
                else:
                    print('Invalid Pin')
            else:
                print('Invalid paytm number')
    def netBanking(self):
        while True:
            acc = input('Enter your account number: ')
            if len(acc) == 12:
                ifsc_code = input('Enter your ifsc_code: ').isalnum()
                if len(ifsc_code) == 10:
                    net_banking_pin = int(input('Enter your net_banking_pin: '))
                    if net_banking_pin == '1108':
                        print(f"The payment for the {self.buy} has been done successfully")
                        self.f.append((self.buy,self.get_price()))
                        break
                    print('Invalid Pin')
                print('Invalid IFSC Code')
            else:
                print('Invalid account number')
    def get_price(self):
        for i in self.product.values():
            for k in i.values():
                if self.buy in k:
                    return k[self.buy]
        return 0
    def add_to_cart(self):
        while True:
            self.products()
            for n in self.product:
                print(n)
            i = input('Enter Category name: ')
            if i in self.product.keys():
                print('There is a sub-category in this category which is:')
                for n in self.product[i]:
                    print(n)
                k = input('Enter the product category: ')
                if k in self.product[i]:
                    print('The products in this category are:')
                    for m in self.product[i][k].items():
                        print(f'{m[0]}: {m[1]}')
                    while True:
                        un = input('Enter the product name you want to add in your cart (or type back to go back): ')
                        if un == 'back':
                            break
                        if un in self.product[i][k]:
                            self.f.append((un,self.product[i][k][un]))
                            print(f'Product added to your cart {un}')
                        else:
                            print('The product is not available')
                    break
                else:
                    print('The product is not available')
            else:
                print(f'There is no such category,{i}.')
    def display_products_added_to_cart(self):
        if not self.f:
            print('There are no products added to your cart.')
        else:
            print('The products added to your cart are: ')
            self.total = 0
            for n,(k,j) in enumerate(self.f,start=1):
                print(f'{n}. {k}-{j}')
                self.total += j
            print(f'Total: {self.total}')
    def generate_receipt(self):
        while True:
            if not self.f:
                print('No products bought.')
            receipt_number = random.randint(100,9999)
            timeS = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S%%")
            total = 0
            filename = f'{self.username}_receipt.txt'
            print('----Generated Receipt----')
            print(f'Receipt number: {receipt_number}')
            print(f'Date: {timeS}')
            print(f'Items Purchased: ')
            print(f'-------------------')
            for n, (k, j) in enumerate(self.f, start=1):
                print(f'{n}.{k}-Rs: {j}')
                total += j
            print('--------------------')
            print(f'Total: {total}')
            print('Thanks you for shopping with us')
            print(f'--------------------')
            with open(filename, 'w') as file:
                file.write('Generated Receipt\n')
                file.write(f'Receipt number: {receipt_number}\n')
                file.write(f'Date: {timeS}\n')
                file.write(f'Items Purchased: \n')
                file.write(f'-------------------\n')
                for n, (k, j) in enumerate(self.f, start=1):
                    file.write(f'{n}.{k}-Rs: {j}\n')
                    total += j
                file.write('--------------------\n')
                file.write(f'Total: {total}\n')
                file.write('Thanks you for shopping with us')
                file.write(f'--------------------')
            print(f'Receipt generated and saved as {filename}')
            break
    def user(self):
        while True:
            self.username = input('Enter Username: ')
            if self.username == 'messi':
                password = input('Enter Password: ')
                if password == 'mess':
                    print(f'Welcome to the Shopping Panel, Mr.{self.username}')
                    print('What would you like to do?')
                    print('1. Display products\n2. Buy Products\n3.Add to cart\n4.Exit')
                    choice = int(input('Enter your choice: '))
                    if choice == 1:
                        self.display_products()
                        break
                    elif choice == 2:
                        while True:
                            self.buy_products()
                            buyMore = input('Do you want to buy more products? (y/n): ')
                            if buyMore != 'y':
                                if self.f:
                                    self.generate_receipt()
                                    break
                                else:
                                    print('No products has been bought')
                                break
                        print('Thanks for the shopping, visit again soon')
                        break
                    elif choice == 3:
                        while True:
                            self.add_to_cart()
                            another = input('Do you want to add another product? (y/n): ')
                            if another != 'y':
                                break
                        self.display_products_added_to_cart()
                        break
                    elif choice == 4:
                        break
                    else:
                        print('Invalid choice')
                else:
                    print('Invalid Password')
            else:
                print('Invalid Username')
    def admin(self):
        while True:
            self.products()
            admin_name = input('Enter Admin Name: ')
            if admin_name == 'keerthana':
                admin_password = input('Enter Admin Password: ')
                if admin_password == '0902':
                    print(f'Welcome {admin_name}')
                    print('What would you like to do?\n1. Add Products to store\n2. View Products in Store\n3. Exit')
                    choice = int(input('Enter your choice: '))
                    if choice == 1:
                        key = input('Enter product category: ')
                        key2 = input('Enter product sub-category: ')
                        product_name = input('Enter product name: ')
                        prod_price = int(input('Enter product price: '))
                        if key not in self.product:
                            self.product[key] = {}
                        if key2 not in self.product[key]:
                            self.product[key][key2] = {}
                        self.product[key][key2][product_name] = prod_price
                        print(f'Product added: {product_name} with price: {prod_price}')
                        break
                    elif choice == 2:
                        print('Products in the store are: ')
                        for key in self.product:
                            # print(f'{key}: {self.product[key]}')
                            print(f'Category: {key} ')
                            for j in self.product[key]:
                                print(f'Product sub-category: {j} ')
                                for prod in self.product[key][j].items():
                                    print(f'{prod[0]}: {prod[1]}')
                        break
                    elif choice == 3:
                        print('Exiting admin panel...')
                        break
                    else:
                        print('Invalid choice')
                else:
                    print('Invalid Password')
            else:
                print('Invalid Admin name')
    def home(self):
        while True:
            print('Welcome who is this?\n1.User\n2.Admin\n3.Exit')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.user()
                break
            elif choice == 2:
                self.admin()
                break
            elif choice == 3:
                break
            else:
                print('Invalid choice')

obj = Panel()
obj.home()