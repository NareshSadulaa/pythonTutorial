import  mysql.connector
__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root@123',
                              host='localhost', port=3306,
                              database='todo_app1')
    return __cnx

def addTask(task):
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = "INSERT INTO todolist (task, task_completed, deleted_task) VALUES (%s, %s, %s)"
    data = (task,'No','No')
    cursor.execute(query,data)
    connection.commit()
    print(f"Task added: {task}")

def fetchTasks():
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = "SELECT task_id, task FROM todo_app1.todolist WHERE deleted_task = 'NO'; "
    cursor.execute(query)
    return cursor.fetchall()

def removeTask(task_id):
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = "UPDATE todolist SET deleted_task = 'YES' WHERE task_id = %s;"
    cursor.execute(query,(task_id,))
    connection.commit()
    print(f"Task removed: {task_id}")

def print_menu():
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')


def get_choice():
    while True:
        choice = input('Enter your choice: ')
        valid_choices = ('1', '2', '3', '4')
        if choice not in valid_choices:
            print('Invalid choice')
            continue
        else:
            return choice


def display_tasks():
    tasks = fetchTasks()
    if not tasks:
        print('No tasks in the list.')
        return
    print('\nYour Tasks:')
    for id, task in tasks:
        print(f'{id}. {task}')


def add_task():
    task = input('Enter a new task: ').strip()
    if task:
        addTask(task)
    else:
        print('Invalid input!')


def remove_task():
    display_tasks()
    try:
        task_id = int(input('Enter task id: '))
        removeTask(task_id)
    except ValueError:
        print('Invalid input! Try again!')

def main():
    while True:
        print_menu()

        choice = get_choice()

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        else:
            break


if __name__ == '__main__':
    main()