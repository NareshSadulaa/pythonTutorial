import mysql.connector

data = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="morning_python",
    port=3306
)
var = data.cursor()
# create_table = "create table employee(emp_id int primary key,emp_name varchar(20),emp_salary int)"
# var.execute(create_table)
# data.commit()

while True:
    choice = int(input("Enter a choice(1.Insert, 2.View, 3.Remove, 4.Update, 5.Exit):- "))
    if choice == 1:
        id = int(input("Enter Employee Id:- "))
        name = input("Enter Employee Name:- ")
        salary = int(input("Enter Employee Salary:- "))
        insert_query = f"insert into employee values({id},'{name}',{salary})"
        var.execute(insert_query)
        data.commit()
    elif choice == 2:
        select_query = f"select * from employee"
        var.execute(select_query)
        data.fetchAll()
    elif choice == 3:
        id = int(input("Enter Employee Id:- "))
        delete_query = f"delete from employee where emp_id = {id}"
        var.execute(delete_query)
        data.commit()
    elif choice == 4:
        id = int(input("Enter Employee Id:- "))
        salary = int(input("Enter Employee Salary:- "))
        update_query = f"update employee set emp_salary = {salary} where emp_id = {id}"
        var.execute(update_query)
        data.commit()
    elif choice == 5:
        break
    else:
        print("Wrong Choice")