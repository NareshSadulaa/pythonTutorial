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
            f = input("Kya aap sachme admin ho?(y/n): ")
            if f == 'y':
                email = input("Humko vishwas nhi hai aapka email-id type karo: ")
                password = input("Apna password type karo: ")
                query9 = f"SELECT admin_id FROM admin_table WHERE admin_email = '{email}' and admin_password = '{password}'"
                self.cursor.execute(query9)
                result = self.cursor.fetchone()
                # print("Chalo mann liya aap hi ho Admin")
                if result:
                    print("\n1. Colleges Dekhna hai"
                          "\n2. College ko remove karna hai"
                          "\n3. Students ko dikhao"
                          "\n4. Students ko remove karna hai"
                          "\n5. Exam centers dikhao"
                          "\n6. Students ko remove karna hai Exam Center se"
                          "\n7. Student ko exam center me add karna hai"
                          "\n8. Exit")
                    choice = int(input("Par aap aaye kyu ho yaha?: "))
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
                        self.removeStudentFromExamCenter()
                    elif choice == 7:
                        self.exam_center()
                        break
                    elif choice == 8:
                        break
                    else:
                        print("Tumhara choice hi galat hai...")
                else:
                    print("Aap admin nhi ho, niklo yaha se...")
            else:
                print("Invalid Entry")

    def register(self):
        print("\n1 Student Registration. \n2 College Registration.")
        choice = int(input("Kon ho aap?: "))
        if choice == 1:
            name = input("Aapka naam bataiye?: ")
            email = input("Aapka email-id register kare?: ")
            if "@gmail" in email:
                password = input("Aapka Password kya hai?: ")
                query = f"INSERT INTO student_table(student_name,student_email,student_password) VALUES('{name}','{email}','{password}')"
                self.cursor.execute(query)
                self.database.commit()
                print(f"Mr {name} has been registered successfully")
            else:
                print("Aapka email galat hai...")
        elif choice == 2:
            name = input("Aapka naam bataiye?: ")
            email = input("Aapka email-id register kare?: ")
            if "@gmail" in email:
                password = input("Aapka Password kya hai?: ")
                query = f"INSERT INTO college_table(college_name,college_email,college_password) VALUES('{name}','{email}','{password}')"
                self.cursor.execute(query)
                self.database.commit()
                print(f"{name} has been registered successfully")
            else:
                print("Aapka email galat hai...")
        else:
            print("Tumhara choice hi galat hai...")

    def student_login(self):
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            query1 = f"SELECT student_id FROM student_table WHERE student_email = '{email}' and student_password = '{password}'"
            self.cursor.execute(query1)
            result = self.cursor.fetchone()
            if result:
                print("Login Successful")
                print("\n1 Aapka Seat Number yaha se check kare..."
                  "\n2 Aapka Exam Center yaha se check kare..."
                      "\n3 Exit")
                ch = int(input("Karna kya hai aapko?"))
                if ch == 1:
                    stud_email = input("Aapka email-id type kare?: ")
                    query2 = f"SELECT seat_number FROM exam_center WHERE student_email = '{stud_email}'"
                    self.cursor.execute(query2)
                    for seat_number in self.cursor.fetchall():
                        print("Tumhara seat number hai ",seat_number[0])
                    break
                elif ch == 2:
                    stud_email = input("Aapka email-id type kare?: ")
                    query3 = f"SELECT college_name from exam_center WHERE student_email = '{stud_email}'"
                    self.cursor.execute(query3)
                    result = [row for row in self.cursor.fetchall()]
                    for center_name in result:
                        print("Tumhara center hai ",center_name[0])
                    break
                elif ch == 3:
                    break
                else:
                    print("Tumhara choice hi galat hai...")
            else:
                print("Tumhara email-id aur password galat hai...")

    def college_login(self):
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            query1 = f"SELECT college_id FROM college_table WHERE college_email = '{email}' and college_password = '{password}'"
            self.cursor.execute(query1)
            result = self.cursor.fetchone()
            if result:
                print("Login Successful")
                print("\n1 Aapke college me exam dene k liye aane wale bacche..."
                  "\n2 Aapke College me bacche hue seats dekhe..."
                      "\n3 Exit")
                ch = int(input("Karna kya hai aapko?"))
                if ch == 1:
                    coll_name = input("Aapka College name type kare?: ")
                    query2 = f"SELECT student_name FROM exam_center WHERE college_name = '{coll_name}'"
                    self.cursor.execute(query2)
                    for bacche in self.cursor.fetchall():
                        print("Tumhare college aane wale bacche ",bacche)
                    break
                elif ch == 2:
                    coll_name = input("Aapka College name type kare?: ")
                    query3 = f"SELECT remaining_seats from college_table WHERE college_name = '{coll_name}'"
                    self.cursor.execute(query3)
                    result = [row for row in self.cursor.fetchall()]
                    for seats in result:
                        print("Aapke college me bachhe hue seats ",seats[0])
                    break
                elif ch == 3:
                    break
                else:
                    print("Tumhara choice hi galat hai...")
            else:
                print("Tumhara email-id aur password galat hai...")

    def displayCollege(self):
        query11 = "SELECT college_name from college_table"
        self.cursor.execute(query11)
        result = self.cursor.fetchall()
        print(result)

    def removeCollege(self):
        id = int(input("College ka id type kare: "))
        # query12 = f"DELETE college_table WHERE college_id = {id}"
        self.cursor.execute(f"DELETE FROM college_table WHERE college_id = {id}")
        self.database.commit()
        print("Aapka college delete ho chuka hai")

    def viewStudents(self):
        query12 = "SELECT student_name FROM student_table"
        self.cursor.execute(query12)
        result = self.cursor.fetchall()
        print(result[0])

    def removeStudents(self):
        id = int(input("Enter Student ID: "))
        self.cursor.execute(f"DELETE FROM student_table WHERE student_id = {id}")
        self.database.commit()
        print("Aapka student delete ho chuka hai")

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

        print(f"Mr {stud_name}, tumhara center hai {center} aur tumhara seat hai {seat_number}. ",)

    def examCenter(self):
        while True:
            print("\n1. Mujhe apna exam center pata karna hai"
              "\n2. Mujhe apna exam seat number pata karna hai"
              "\n3. Exit")
            choice = int(input("Kya irada hai?: "))
            if choice == 1:
                name = input("Exam Center jaane k liye apna naam type kare: ")
                if name in f"SELECT college_name from exam_center WHERE student_name = '{name}'":
                    # query14 = "SELECT college_name from exam_center"
                    self.cursor.execute("SELECT college_name from exam_center")
                    result = self.cursor.fetchone()
                    for row in result:
                        print("Tumhara exam center hai",row)
                break
            elif choice == 2:
                name = input("Seat Number jaane k liye apna naam type kare: ")
                if name in f"SELECT seat_number from exam_center WHERE student_name = '{name}'":
                    query15 = "SELECT seat_number from exam_center"
                    self.cursor.execute(query15)
                    result = self.cursor.fetchone()
                    for row in result:
                        print("Tumhara seat number hai",row)
                break
            elif choice == 3:
                break
            else:
                print("Tumhara choice hi galat hai...")

    def removeStudentFromExamCenter(self):
        name = input("Enter your name: ")
        query16 = f"DELETE FROM exam_center WHERE student_name = '{name}'"
        self.cursor.execute(query16)
        self.database.commit()

    def home(self):
        while True:
            print("\n1 Me hu admin"
                    "\n2 Me hu Student"
                    "\n3 Mera College hai"
                    "\n4 Mujhe apne aap ko register karwana hai"
                    "\n5 Mujhe apna seat Number aur Exam Center Dekhha hai"
                    "\n6 Exit"
            )
            choice = int(input("Kon ho aap?: "))
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
                print("Tumhara choice hi galat hai...")

obj = University()
obj.home()