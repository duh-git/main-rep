import tkinter as tk
import mysql.connector


class TaskManager(tk.Tk):
    def     __init__(self):
        super().__init__()

        self.connect = mysql.connector.connect(
            host="localhost",
            user="root",
            database="project"
        )

        self.index = 1
        self.work_list = []
        self.slave_list = tk.StringVar()
        self.targets = []
    # Main cofiguration's
        width, height = 1000, 400
        posx, posy = 1550 - width, 40
        title = 'Task Creator'
        self.bg_color = '#10151A'

        self.geometry(f'{width}x{height}+{posx}+{posy}')
        self.resizable(False, False)
        self.title(title)
        self.config(bg=self.bg_color)

        self.task_name = None
        self.deadline = None
        self.description = None
        self.hero_widget()
        self.create_table()

        self.listbox = tk.Listbox(worker_list, listvariable=self.slave_list)
        self.scrollbar = tk.Scrollbar(worker_list, orient="vertical", command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox["yscrollcommand"] = self.scrollbar.set

    # def mark_achieved(self):
    #     selected_target = self.listbox.curselection()
        # if selected_target:
            # target_id = self.targets[selected_target[0]][0]
            # cursor = self.connect.cursor()
            # cursor.execute(
            #     "UPDATE workers SET task_name = %s, actieve_tasks = %s WHERE id = %s", (self.task_name, cursor))
            # self.connect.commit()
            # self.update_targets_list()

    def hero_widget(self):
        self.label_create_task = tk.Label(self, text='Create New Task', bg=self.bg_color, fg='#fff', font=('Arial', 32, 'bold'))
        self.button_create_task = tk.Button(self, text='+', font=('Arial', 65, 'bold'), command=Form)

        self.label_create_task.place(relx=0.5, rely=0.25, anchor='center')
        self.button_create_task.place(relx=0.5, rely=0.65, anchor='center')


    def create_table(self):
        cursor = self.connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS workers
                          (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), actieve_tasks BOOLEAN, task_name VARCHAR(255))''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                          (id INT AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), deadline DATE, description TEXT)''')
        self.connect.commit()

    def main_widget(self):
        bg_element = '#182632'
        self.canvas_task_descryption = tk.Canvas(self, width=300, height=200, bg=bg_element)
        self.label_create_task = tk.Label(self.canvas_task_descryption, text='Task', bg=bg_element, fg='#fff', font=('Arial', 32, 'bold'))
        self.label_task_name = tk.Label(self.canvas_task_descryption, text=self.task_name, bg=bg_element, fg='#fff', font=('Arial', 24, 'normal'))
        self.label_deadline = tk.Label(self.canvas_task_descryption, text=self.deadline, bg=bg_element, fg='#fff', font=('Arial', 24, 'normal'))
        self.label_description = tk.Label(self.canvas_task_descryption, text=self.description, bg=bg_element, fg='#fff', font=('Arial', 24, 'normal'))

        self.canvas_task_descryption.place(relx=0.05, rely=0.05, anchor='nw')
        self.label_create_task.place(relx=0.05, rely=0.05, anchor='nw')
        self.label_task_name.place(relx=0.05, rely=0.35, anchor='nw')
        self.label_deadline.place(relx=0.05, rely=0.55, anchor='nw')
        self.label_description.place(relx=0.05, rely=0.75, anchor='nw')

    def read_bd(self):
        work_list = []
        slave_list = []
        cursor = self.connect.cursor()
        cursor.execute('''SELECT name, active_tasks, task_name from workers''')
        result = cursor.fetchall()
        for row in result:
            if not row[1]:
                work_list.append([row[0], row[2]])
            else:
                slave_list.append([row[0], row[2]])
        self.work_list = work_list
        self.slave_list.set(slave_list)
        self.card(self, work_list[0][0])


    def add_task(self):
        cursor = self.connect.cursor()
        cursor.execute("INSERT INTO tasks (task_name, deadline, description) VALUES (%s, %s, %s)",
                       (self.task_name, self.deadline, self.description))

        # "UPDATE workers SET achieve_tasks = 0, task_name = '' WHERE id = %s", (target_id,))

        # "UPDATE workers SET achieve_tasks = 1, task_name = %s, WHERE id = %s", (target_id, task_name))



        self.connect.commit()

        self.label_create_task.destroy()
        self.button_create_task.destroy()
        self.main_widget()
        self.read_bd()

    def card(self, master, name):
        bg_color = '#182632'

        self.canvas = tk.Canvas(master, width=300, height=300, bg=bg_color)
        self.label_name = tk.Label(self.canvas, text=name, bg=bg_color, fg='#fff', font=('Arial', 24, 'normal'))
        self.button_yes = tk.Button(self.canvas, text='Yes', font=('Arial', 24, 'normal'), command=app.stop)
        self.button_no = tk.Button(self.canvas, text='No', font=('Arial', 24, 'normal'), command=app.next)

        self.canvas.place(relx=0.5, rely=0.05, anchor='nw')
        self.label_name.place(relx=0.5, rely=0.10, anchor='center')
        self.button_yes.place(relx=0.5, rely=0.5, anchor='s')
        self.button_no.place(relx=0.5, rely=0.85, anchor='s')
 # ccВыберите поле основного индекса (PRIMARY) или уникального индекса!
    def next(self):
        self.canvas.destroy()
        self.label_name.destroy()
        self.button_yes.destroy()
        self.button_no.destroy()
        self.index += 1
        if self.index == len(self.work_list):
            self.index = 0
        self.card(self, self.work_list[self.index][0])


    def stop(self):
        self.canvas.destroy()
        self.label_name.destroy()
        self.button_yes.destroy()
        self.button_no.destroy()
        self.canvas_task_descryption.destroy()
        self.label_create_task.destroy()
        self.label_task_name.destroy()
        self.label_deadline.destroy()
        self.label_description.destroy()
        # self.mark_achieved()
        self.hero_widget()
        # cursor = self.connect.cursor()
        # cursor.execute("UPDATE workers SET active_tasks = 1, task_name = %s, WHERE id = %s", (1, self.task_name))

class Form(tk.Tk):
    def __init__(self):
        super().__init__()

        width, height = 800, 500
        posx, posy = 1450 - width, 40
        title = 'GUI'
        self.bg_color = '#10151A'

        self.geometry(f'{width}x{height}+{posx}+{posy}')
        self.resizable(False, False)
        self.title(title)
        self.config(bg=self.bg_color)

        self.widget()

    def widget(self):
        self.label_create_task = tk.Label(self, text='Create New Task', bg=self.bg_color, fg='#fff', font=('Arial', 32, 'bold'))
        self.label_task_name = tk.Label(self, text='Task Name', bg=self.bg_color, fg='#fff', font=('Arial', 24, 'bold'))
        self.label_deadline = tk.Label(self, text='Deadline', bg=self.bg_color, fg='#fff', font=('Arial', 24, 'bold'))
        self.label_description = tk.Label(self, text='Description', bg=self.bg_color, fg='#fff', font=('Arial', 24, 'bold'))
        self.entry_task_name = tk.Entry(self, font=('Arial', 28, 'normal'))
        self.entry_deadline = tk.Entry(self, font=('Arial', 28, 'normal'))
        self.entry_description = tk.Entry(self, font=('Arial', 28, 'normal'))
        self.button_submit = tk.Button(self, text='Submit', font=('Arial', 28, 'bold'), command=self.go)

        self.label_create_task.place(relx=0.5, rely=0.15, anchor='center')
        self.label_task_name.place(relx=0.05, rely=0.35, anchor='w')
        self.label_deadline.place(relx=0.05, rely=0.5, anchor='w')
        self.label_description.place(relx=0.05, rely=0.65, anchor='w')
        self.entry_task_name.place(relx=0.38, rely=0.35, anchor='w')
        self.entry_deadline.place(relx=0.38, rely=0.5, anchor='w')
        self.entry_description.place(relx=0.38, rely=0.65, anchor='w')
        self.button_submit.place(relx=0.5, rely=0.85, anchor='center')

    def go(self):
        app.task_name = self.entry_task_name.get()
        app.deadline = self.entry_deadline.get()
        app.description = self.entry_description.get()
        self.destroy()

        app.add_task()



class TaskList(tk.Tk):
    def __init__(self):
        super().__init__()

        width, height = 400, 600
        posx, posy = 500 - width, 40
        title = 'Worker\'s List'
        self.bg_color = '#10151A'

        self.geometry(f'{width}x{height}+{posx}+{posy}')
        self.resizable(False, False)
        self.title(title)
        self.config(bg=self.bg_color)






if __name__ == '__main__':
    worker_list = TaskList()
    app = TaskManager()
    app.mainloop()


