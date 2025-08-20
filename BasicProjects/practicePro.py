import mysql.connector
import random

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="practice_database",
    port=3306
)
var = database.cursor()

random_number = random.randint(1, 100)
query = 'SELECT * FROM practice_table2'
var.execute(query)
names = [row for row in var.fetchall()]
random_name = random.choice(names)[0]
print(random_name)
print(random_number)
results = query2 = f"INSERT INTO practice_table3 values({random_number},'{random_name}')"
var.execute(query2)
database.commit()

user = input("Enter your name: ")
for name, random_number in results:
    if name == user:
        print(f"your seat number ")
        break
else:
    print("Not found")
