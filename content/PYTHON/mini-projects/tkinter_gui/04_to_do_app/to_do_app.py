import psycopg2
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

host = 'localhost'
user = 'postgres'
password = 'admin'
database = 'py_todo'
port = 5432
connection = None
cursor = None
sql_date = '%Y-%m-%d'


connection = psycopg2.connect(host=host, user=user, password=password, port=port)
connection.autocommit = True
cursor = connection.cursor() 

cursor.close()
connection.close()

connection = psycopg2.connect(host=host, user=user, password=password, port=port, database=database)
cursor = connection.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            due_date DATE NOT NULL           
        );
    ''')
    connection.commit()

def add_task(title, content, due_date):
    if not due_date:
        due_date = datetime.now().strftime(sql_date)

    cursor.execute('''
        INSERT INTO tasks (title, content, due_date)
            VALUES(%s, %s, %s);
    ''', (title, content, due_date))

    connection.commit()
    load_tasks()

def update_task(task_id, title, content, due_date):
    if not due_date:
        due_date = datetime.now().strftime(sql_date)

    cursor.execute('''
        UPDATE tasks SET title = %s, content = %s, due_date = %s
            WHERE id = %s;
    ''', (title, content, due_date, task_id))
    connection.commit()
    load_tasks()

def delete_task(task_id):
    cursor.execute('''
        DELETE FROM tasks WHERE id = %s
    ''', (task_id,))
    connection.commit()
    load_tasks()

def load_tasks():
    '''Ładuje zadania z bazy danych i wyświetla je w interfejsie użytkownika'''
    cursor.execute('SELECT * FROM tasks ORDER BY id ASC;')
    tasks = cursor.fetchall()

    for widget in frame_tasks.winfo_children():
        widget.destroy()

    for task in tasks:
        task_frame = tk.Frame(frame_tasks, bg='white', pady=10)
        task_frame.pack(fill='x')

        tk.Label(task_frame, text=f'{task[1]} (To-do: {task[3]})', bg='white').pack(side='left')
        tk.Button(task_frame, text='Edit', command= lambda task=task: edit_task(task)).pack(side='right')
        tk.Button(task_frame, text='Delete', command= lambda task_id=task[0]: delete_task(task_id)).pack(side='right')

def edit_task(task):
    entry_title.delete(0, tk.END)
    entry_title.insert(0, task[1])
    entry_content.delete(0, tk.END)
    entry_content.insert(0, task[2])
    entry_due_date.delete(0, tk.END)
    entry_due_date.insert(0, task[3])
    button_add_task.config(text='Save', width=25, 
                            command= lambda: update_task(task[0], entry_title.get(), 
                                                         entry_content.get(), entry_due_date.get()))
    
root = tk.Tk()
root.title('Managing tasks.')
root.geometry('1024x768')

frame_add_task = tk.Frame(root, padx=10, pady=10)
frame_add_task.pack(fill='x')

tk.Label(frame_add_task, text='Title:').pack(side='left')
entry_title = tk.Entry(frame_add_task)
entry_title.pack(side='left', expand=True, fill='x')

tk.Label(frame_add_task, text='Content:').pack(side='left')
entry_content = tk.Entry(frame_add_task)
entry_content.pack(side='left', expand=True, fill='x')

tk.Label(frame_add_task, text='Due-date:').pack(side='left')
entry_due_date = tk.Entry(frame_add_task)
entry_due_date.pack(side='left', expand=True, fill='x')

button_add_task = tk.Button(frame_add_task, text='Add', width=20,
                            command= lambda: add_task(entry_title.get(), entry_content.get(), entry_due_date.get()))
button_add_task.pack(side='right')

frame_tasks = tk.Frame(root, bg='white')
frame_tasks.pack(fill='both', expand=True)

create_table()
load_tasks()

def on_closing():
    if messagebox.askokcancel('Quit', 'Are you sure?'):
        cursor.close()
        connection.close()
        root.destroy()

root.protocol('WM_DELETE_WINDOW', on_closing)
root.mainloop()
