import mysql.connector

var = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="morning_python",
    port="3306"
)

var1 = var.cursor()

# table = "create table emp(emp_id int primary key, emp_name varchar(20), emp_salary int)"
# var1.execute(table)

while True:
    choice = input("Enter your choice(1.Insert, 2.Update, 3.Remove, 4.View, 5.Exit): ")
    if choice == "1":
        id = int(input("Enter Employee id: "))
        name = input("Enter Employee name: ")
        salary = int(input("Enter Employee salary: "))
        query = f"insert into emp values({id},'{name}',{salary})"
        var1.execute(query)
        var.commit()
    elif choice == "2":
        salary = int(input("Enter Employee salary: "))
        id = int(input("Enter Employee id: "))
        query2 = f"update emp set emp_salary = {salary} where emp_id = {id}"
        var1.execute(query2)
        var.commit()
    elif choice == "3":
        id = int(input("Enter Employee id: "))
        query3 = f"delete from emp where emp_id = {id}"
        var1.execute(query3)
        var.commit()
    elif choice == "4":
        query4 = f"select * from emp"
        var1.execute(query4)
        var.commit()
    elif choice == "5":
        exit()
    else:
        print("Wrong choice")
