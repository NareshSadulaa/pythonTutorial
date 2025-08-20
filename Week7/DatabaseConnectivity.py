# pip install mysql-connector-python

import mysql.connector

var = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="morning_python",
    port=3306
)
var1 = var.cursor()
# query = "create table student2(roll_no int primary key, student_name varchar(20),location varchar(20));)"
# query1 = "insert into student2 (roll_no, student_name, location) values (3,'Dipesh','Thane'),"
# var1.execute(query1)
# var.commit()

# query2 = "update student2 set location= 'Mumbai' where roll_no = 1"
# var1.execute(query2)
# var.commit()

# query3 = "delete from student2 where roll_no = 2"
query3 = "insert into student2(roll_no, n  fstudent_name,location) values(01,'Naresh','Bhiwandi')"

var1.execute(query3)
var.commit()
