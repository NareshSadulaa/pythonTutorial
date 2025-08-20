import random
import mysql.connector

class University:
    def __init__(self):
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database="exam_management",
            port= 3306
        )
        self.cursor = self.database.cursor()
        self.database.commit()

    def adminLogin(self):
        while True:
            f = input("Are you really an admin?(y/n): ")
            if f == 'y':
                email = input("Enter your Email-Id: ")
                password = input("Enter your Password: ")
                query9 = f"SELECT admin_id FROM admin_table WHERE admin_email = '{email}' and admin_password = '{password}'"
                self.cursor.execute(query9)
                result = self.cursor.fetchone()
                # print("Chalo mann liya aap hi ho Admin")
                if result:
                    print("\n1. Display Colleges"
                          "\n2. Remove Colleges"
                          "\n3. View Students"
                          "\n4. Remove Students"
                          "\n5. Display Exam Centers"
                          "\n6. Add Students to exam centers"
                          "\n7. Remove Students from exam centers"
                          "\n8. Exit")
                    choice = int(input("What you want to do?: "))
                    if choice == 1:
                        self.displayCollege()
                        break
                    elif choice == 2:
                        self.removeCollege()
                        break
                    elif choice == 3:
                        self.viewStudents()
                        break
                    elif choice == 4:
                        self.removeStudents()
                        break
                    elif choice == 5:
                        self.examCenters()
                        break
                    elif choice == 6:
                        self.exam_center()
                        break
                    elif choice == 7:
                        self.removeStudentFromExamCenter()
                        break
                    elif choice == 8:
                        break
                    else:
                        print("Invalid Choice")
                else:
                    print("You're Email-Id and Password doesn't match")
            else:
                print("Invalid Entry")

    def register(self):
        print("\n1 Student Registration. \n2 College Registration.")
        choice = int(input("Who wants to register?: "))
        if choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email-id?: ")
            if "@gmail" in email:
                password = input("Enter your password: ")
                query = f"INSERT INTO student_table(student_name,student_email,student_password) VALUES('{name}','{email}','{password}')"
                self.cursor.execute(query)
                self.database.commit()
                print(f"Mr {name} has been registered successfully")
            else:
                print("Invalid Email")
        elif choice == 2:
            name = input("Enter your college name: ")
            email = input("Enter your college's email-id: ")
            if "@gmail" in email:
                password = input("Enter your password: ")
                query = f"INSERT INTO college_table(college_name,college_email,college_password) VALUES('{name}','{email}','{password}')"
                self.cursor.execute(query)
                self.database.commit()
                print(f"{name} has been registered successfully")
            else:
                print("Invalid Email-Id")
        else:
            print("Invalid Choice")

    def student_login(self):
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            query1 = f"SELECT student_id FROM student_table WHERE student_email = '{email}' and student_password = '{password}'"
            self.cursor.execute(query1)
            result = self.cursor.fetchone()
            if result:
                print("Login Successful")
                print("\n1 Check your seat number here.."
                  "\n2 Check your exam center here..."
                      "\n3 Exit")
                ch = int(input("What do you want to know?: "))
                if ch == 1:
                    stud_email = input("Enter your email-id: ")
                    query2 = f"SELECT seat_number FROM exam_center WHERE student_email = '{stud_email}'"
                    self.cursor.execute(query2)
                    for seat_number in self.cursor.fetchall():
                        print("You're seat number is ",seat_number[0])
                    break
                elif ch == 2:
                    stud_email = input("Enter your email-id: ")
                    query3 = f"SELECT college_name from exam_center WHERE student_email = '{stud_email}'"
                    self.cursor.execute(query3)
                    result = [row for row in self.cursor.fetchall()]
                    for center_name in result:
                        print("You're examination center is ",center_name[0])
                    break
                elif ch == 3:
                    break
                else:
                    print("Invalid Choice")
            else:
                print("Invalid Email-Id and Password")

    def college_login(self):
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            query1 = f"SELECT college_id FROM college_table WHERE college_email = '{email}' and college_password = '{password}'"
            self.cursor.execute(query1)
            result = self.cursor.fetchone()
            if result:
                print("Login Successful")
                print("\n1 View students who are allotted to your college for examination"
                  "\n2 View remaining seats in your college for examination"
                      "\n3 Exit")
                ch = int(input("What do you want to know?: "))
                if ch == 1:
                    coll_name = input("Enter your college name: ")
                    query2 = f"SELECT student_name FROM exam_center WHERE college_name = '{coll_name}'"
                    self.cursor.execute(query2)
                    for student in self.cursor.fetchall():
                        print("Students who are coming to give exams in your college ",student)
                    break
                elif ch == 2:
                    coll_name = input("Enter your college name: ")
                    query3 = f"SELECT remaining_seats from college_table WHERE college_name = '{coll_name}'"
                    self.cursor.execute(query3)
                    result = [row for row in self.cursor.fetchall()]
                    for seats in result:
                        print("Remaining seats in your college   ",seats[0])
                    break
                elif ch == 3:
                    break
                else:
                    print("Invalid Choice")
            else:
                print("Invalid email-id or password")

    def displayCollege(self):
        query11 = "SELECT college_name from college_table"
        self.cursor.execute(query11)
        result = self.cursor.fetchall()
        print(result)

    def removeCollege(self):
        id = int(input("Enter college Id: "))
        # query12 = f"DELETE college_table WHERE college_id = {id}"
        self.cursor.execute(f"DELETE FROM college_table WHERE college_id = {id}")
        self.database.commit()
        print("College has been removed")

    def viewStudents(self):
        query12 = "SELECT student_name FROM student_table"
        self.cursor.execute(query12)
        result = self.cursor.fetchall()
        print(result[0])

    def removeStudents(self):
        id = int(input("Enter Student ID: "))
        self.cursor.execute(f"DELETE FROM student_table WHERE student_id = {id}")
        self.database.commit()
        print("Student has been removed")

    def examCenters(self):
        query13 = "SELECT college_name from exam_center"
        self.cursor.execute(query13)
        result = self.cursor.fetchall()
        print(result[0])

    def exam_center(self):
        seat_number = random.randint(10000,20000)
        query4 = "SELECT college_name from college_table"
        self.cursor.execute(query4)
        result = [row for row in self.cursor.fetchall()]
        center = random.choice(result)[0]

        query5 = "SELECT student_name from student_table"
        self.cursor.execute(query5)
        student_names = [row for row in self.cursor.fetchall()]
        stud_name = random.choice(student_names)[0]
        # name = random.choice(student_names)[0]

        query6 = "SELECT student_email from student_table"
        self.cursor.execute(query6)
        stud_emails = [row for row in self.cursor.fetchall()]
        stud_email = random.choice(stud_emails)[0]

        query7 = f"INSERT INTO exam_center VALUES({seat_number},'{stud_name}','{center}','{stud_email}')"
        self.cursor.execute(query7)
        self.database.commit()

        print(f"Mr {stud_name}, you're examination center is {center} and you're seat number is {seat_number}. ",)

    def examCenter(self):
        while True:
            print("\n1. I want to know my examination center"
              "\n2. I want to know my seat number"
              "\n3. Exit")
            choice = int(input("What do you want to know?: "))
            if choice == 1:
                name = input("Enter your name to check your examination center: ")
                if name in f"SELECT college_name from exam_center WHERE student_name = '{name}'":
                    # query14 = "SELECT college_name from exam_center"
                    self.cursor.execute("SELECT college_name from exam_center")
                    result = self.cursor.fetchone()
                    for row in result:
                        print("You're examination center is ",row)
                break
            elif choice == 2:
                name = input("Enter your name to check your seat number: ")
                if name in f"SELECT seat_number from exam_center WHERE student_name = '{name}'":
                    query15 = "SELECT seat_number from exam_center"
                    self.cursor.execute(query15)
                    result = self.cursor.fetchone()
                    for row in result:
                        print("You're Seat number is ",row)
                break
            elif choice == 3:
                break
            else:
                print("Invalid Choice")

    def removeStudentFromExamCenter(self):
        name = input("Enter your name: ")
        query16 = f"DELETE FROM exam_center WHERE student_name = '{name}'"
        self.cursor.execute(query16)
        self.database.commit()

    def home(self):
        while True:
            print("\n1 I'm the admin"
                    "\n2 I am a Student"
                    "\n3 I am a College official"
                    "\n4 I want to register myself"
                    "\n5 I want to know about my examination center"
                    "\n6 Exit"
            )
            choice = int(input("Who are you?: "))
            if choice == 1:
                self.adminLogin()
            elif choice == 2:
                self.student_login()
            elif choice == 3:
                self.college_login()
            elif choice == 4:
                self.register()
            elif choice == 5:
                self.examCenter()
            elif choice == 6:
                break
            else:
                print("Invalid Choice")

obj = University()
obj.home()
