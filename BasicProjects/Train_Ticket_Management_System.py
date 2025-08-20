# import mysql.connector
# from datetime import datetime
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root@123",
#     database="train_ticket_management"
# )
# cursor = db.cursor()
#
# def register():
#     id = int(input("Enter ID: "))
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     cursor.execute(f"INSERT INTO users VALUES({id},'{name}','{email}','{password}')")
#     db.commit()
#
# def user_login():
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     cursor.execute(f"SELECT user_id FROM users WHERE user_email='{email}' and user_password='{password}'")
#     result = cursor.fetchone()
#     if result:
#         print("Login Successful")
#         return result[0]
#     else:
#         print("Login Unsuccessful")
#         return None
#
# def search_trains():
#     source = input("Enter your search source: ")
#     destination = input("Enter your search destination: ")
#     query = f"SELECT * FROM trains_table WHERE train_source = '{source}' AND train_destination = '{destination}'"
#     cursor.execute(query)
#     results = cursor.fetchall()
#     if not results:
#         print("Trains not found your destination.")
#         return []
#     else:
#         print("Available Trains are...")
#         for n in results:
#             print(f"Train ID: {n[0]}, Train Name: {n[1]},departure: {n[5]}, arrival: {n[6]},seats left: {n[8]}")
#         return results
#     # print()
#
# search_trains()
# # user_login()
# # register()
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="train_ticket_management"
)
cursor = db.cursor()

# Register new user
def register():
    id = int(input("Enter ID: "))
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (id, name, email, password))
        db.commit()
        print("Registration successful.\n")
    except mysql.connector.errors.IntegrityError:
        print("Error: ID or email already exists.\n")

# User login
def user_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT user_id FROM users WHERE user_email = %s AND user_password = %s", (email, password))
    result = cursor.fetchone()
    if result:
        print("Login Successful.\n")
        return result[0]
    else:
        print("Login Failed.\n")
        return None

# Search trains
def search_trains():
    source = input("Enter source station: ")
    destination = input("Enter destination station: ")
    cursor.execute("SELECT * FROM trains_table WHERE train_source = %s AND train_destination = %s", (source, destination))
    results = cursor.fetchall()

    if not results:
        print("No trains found.\n")
        return []
    else:
        print("\nAvailable Trains:")
        for train in results:
            print(f"Train ID: {train[0]}, Name: {train[1]}, Departure: {train[4]}, Arrival: {train[5]}, Available Seats: {train[7]}")
        return results

# Book a ticket
def book_ticket(user_id):
    trains = search_trains()
    if not trains:
        return

    train_id = int(input("\nEnter Train ID to book: "))
    cursor.execute("SELECT available_seats FROM trains_table WHERE train_id = %s", (train_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        cursor.execute("INSERT INTO tickets (user_id, train_id, booking_time) VALUES (%s, %s, %s)",
                       (user_id, train_id, datetime.now()))
        cursor.execute("UPDATE trains_table SET available_seats = available_seats - 1 WHERE train_id = %s", (train_id,))
        db.commit()
        print("Ticket booked successfully.\n")
    else:
        print("No available seats on this train.\n")

# View booked tickets
def view_tickets(user_id):
    cursor.execute("""
        SELECT t.ticket_id, tr.train_name, tr.train_source, tr.train_destination, tr.departure_time, tr.arrival_time, t.booking_time
        FROM tickets t
        JOIN trains_table tr ON t.train_id = tr.train_id
        WHERE t.user_id = %s
    """, (user_id,))
    results = cursor.fetchall()

    if results:
        print("\nYour Booked Tickets:")
        for ticket in results:
            print(f"Ticket ID: {ticket[0]}, Train: {ticket[1]}, From: {ticket[2]}, To: {ticket[3]}, Departs: {ticket[4]}, Arrives: {ticket[5]}, Booked On: {ticket[6]}")
    else:
        print("No tickets found.\n")

# Main Menu
def main():
    while True:
        print("\n--- Train Ticket Management ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user_id = user_login()
            if user_id:
                while True:
                    print("\n1. Search Trains\n2. Book Ticket\n3. View My Tickets\n4. Logout")
                    user_choice = input("Enter choice: ")
                    if user_choice == '1':
                        search_trains()
                    elif user_choice == '2':
                        book_ticket(user_id)
                    elif user_choice == '3':
                        view_tickets(user_id)
                    elif user_choice == '4':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
