import tkinter as tk
import pymysql as sql


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        margin = 100
        self.width, self.height = self.winfo_screenwidth() - (margin * 2), self.winfo_screenheight() - (margin * 2)

        self.geometry(f'{self.width}x{self.height}+{margin}+{margin}')
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file="img/mospolytech-logo-white.png"))
        self.title('Task Manager')

        self.config(bg='#10151A')

        self.config_title = dict(font=('Arial', 36, 'bold'), fg='#fff', bg=self['bg'])
        self.config_label = dict(font=('Arial', 16, 'normal'), fg='#fff', bg=self['bg'])
        self.config_input = dict(font=('Arial', 16, 'normal'), width=25)

        self.display()

    def display(self):
        TaskAdd().place(relx=0, rely=0)


class TaskAdd(tk.Frame):
    def __init__(self):
        super().__init__()

        self['width'] = self.master.width * 2 // 3
        self['height'] = self.master.height
        self['bg'] = self.master['bg']
        self['bg'] = '#10151f'

        self.config_hero_button = dict(font=('Arial', 64, 'bold'), width=4)

        self.get_data()
        self.display_hero()
        # self.display_description()
        # self.display_offer()

    def display_hero(self):
        self.hero_title_label = tk.Label(self, text='Create New Task', cnf={**self.master.config_title})
        self.hero_button = tk.Button(self, text='+', command=self.display_description, cnf={**self.config_hero_button})

        self.hero_title_label.place(relx=0.5, rely=0.3, anchor='center')
        self.hero_button.place(relx=0.5, rely=0.55, anchor='center')

    def display_description(self):
        destroy_object = [self.hero_title_label, self.hero_button]
        for object_name in destroy_object:
            object_name.destroy()

        #Lable's
        self.description_title = tk.Label(self, text='Task Data', cnf=self.master.config_title)
        self.description_label_name = tk.Label(self, text='Task name', cnf=self.master.config_label)
        self.description_label_deadline = tk.Label(self, text='Deadline', cnf=self.master.config_label)
        self.description_label_description = tk.Label(self, text='Description', cnf=self.master.config_label)

        self.description_title.place(relx=0.5, rely=0.1, anchor='center')
        self.description_label_name.place(relx=0.45, rely=0.2, anchor='e')
        self.description_label_deadline.place(relx=0.45, rely=0.3, anchor='e')
        self.description_label_description.place(relx=0.45, rely=0.4, anchor='e')

        self.description_input_name = tk.Entry(self, cnf={**self.master.config_input})
        self.description_input_deadline = tk.Entry(self, cnf={**self.master.config_input})
        self.description_input_description = tk.Text(self, cnf={**self.master.config_input}, height=6)

        self.description_input_name.place(relx=0.55, rely=0.2, anchor='w')
        self.description_input_deadline.place(relx=0.55, rely=0.3, anchor='w')
        self.description_input_description.place(relx=0.55, rely=0.4, anchor='nw')

    def get_data(self):
        try:
            connection = sql.connect(
                host="localhost",
                port=3306,
                user="root",
                database='Project',
                cursorclass=sql.cursors.DictCursor
            )
            print('Connect SUCCESFUL')

        except Exception as error:
            print(error)
            print('Connection FAILED')


if __name__ == '__main__':
    App().mainloop()