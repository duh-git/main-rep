import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        margin = 100
        self.geometry(f'{self.winfo_screenwidth() - (margin * 2)}x{self.winfo_screenheight() - (margin * 2)}'
                      f'+{margin}+{margin}')
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file="img/mospolytech-logo-white.png"))
        self.title('Task Manager')

        self.config(bg='#10151A')

        self.config_label_title = dict(font=('Arial', 32, 'bold'), fg='#fff', bg=self['background'])
        self.config_label_regular = dict(font=('Arial', 24, 'normal'), fg='#fff', bg=self['background'])
        self.config_entry_regular = dict(font=('Arial', 24, 'normal'))
        self.config_button_regular = dict(font=('Arial', 24, 'bold'))
        self.config_button_hero = dict(font=('Arial', 64, 'bold'), padx=22)

        # tk.Label(master, text='asd', font(''Arial', 32, 'bold''), fg='#fff', )

        self.display()

    def display(self):
        TaskAdd().grid(column=1)


class TaskAdd(tk.Frame):
    def __init__(self):
        super().__init__()
        self['background'] = self.master['background']
        # self['background'] = '#fff'
        self['width'] = 500
        self['height'] = 700

        self.hero_display()


    def hero_display(self):
        self.hero_label = tk.Label(self, text='Create Task', cnf={**self.master.config_label_title})
        self.hero_button = tk.Button(self, text='+', command=self.main_display, cnf={**self.master.config_button_hero})

        self.hero_label.place(relx=0.5, rely=0.2, anchor='center')
        self.hero_button.place(relx=0.5, rely=0.55, anchor='center')

    def main_display(self):

        self.hero_label.destroy()
        self.hero_button.destroy()

        label_title = tk.Label(self, text='Task Description', cnf={**self.master.config_label_title})
        label_task_name = tk.Label(self, text='Task name', cnf={**self.master.config_label_regular})
        label_deadline = tk.Label(self, text='Deadline', cnf={**self.master.config_label_regular})
        label_description = tk.Label(self, text='Description', cnf={**self.master.config_label_regular})
        self.entry_task_name = tk.Entry(self, cnf={**self.master.config_entry_regular})
        self.entry_deadline = tk.Entry(self, cnf={**self.master.config_entry_regular})
        self.text_description = tk.Text(self, height=5, wrap='word', cnf={**self.master.config_entry_regular})
        text_scrollbar = tk.Scrollbar(command=self.text_description.yview)
        self.text_description.config(yscrollcommand=text_scrollbar.set)
        button_reset = tk.Button(self, text='Reset', command=self.reset, cnf={**self.master.config_button_regular})
        button_submit = tk.Button(self, text='Submit', command=self.submit, cnf={**self.master.config_button_regular})
        label_title.place(relx=0.05, rely=0.05)
        label_task_name.place(relx=0.12, rely=0.24)
        label_deadline.place(relx=0.12, rely=0.4)
        label_description.place(relx=0.12, rely=0.56)

        self.entry_task_name.place(relx=0.5, rely=0.24, width=200)
        self.entry_deadline.place(relx=0.5, rely=0.4, width=200)
        self.text_description.place(relx=0.5, rely=0.56, width=200)
        text_scrollbar.place()
        button_reset.place(relx=0.45, rely=0.85, anchor='e')
        button_submit.place(relx=0.55, rely=0.85, anchor='w')

        self.entry_task_name.focus()

    def reset(self):
        self.entry_task_name.delete(0, 'end')
        self.entry_deadline.delete(0, 'end')
        self.entry_description.delete(0, 'end')

    def submit(self):
        task_name = self.entry_task_name.get()
        deadline = self.entry_deadline.get()
        description = self.entry_description.get()
        self.destroy()

class Employee(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class a(tk.Frame):
    def __init__(self):
        super().__init__()

        # Create main window
        width, height = 600, 400
        padding = [50, 40]
        # x = 1600 - padding[0] - width
        x = int(800 - width * 0.5)
        y = padding[1]
        # self.geometry(f'{width}x{height}+{x}+{y}')
        # self.resizable(False, False)
        # self.config(bg=bg_color)
        #
        # self.title('Create Task Form')
        # # photo = tk.PhotoImage(file='img/mospolytech-logo-white.png')
        # # self.iconphoto(False, photo)
        #
        # self.display()
    #
    # def display(self):
    #     label_title = tk.Label(self, text='Task Description', cnf={**config_label_title})
    #     label_task_name = tk.Label(self, text='Task name', cnf={**config_label_regular})
    #     label_deadline = tk.Label(self, text='Deadline', cnf={**config_label_regular})
    #     label_description = tk.Label(self, text='Description', cnf={**config_label_regular})
    #     self.entry_task_name = tk.Entry(self, cnf={**config_entry_regular})
    #     self.entry_deadline = tk.Entry(self, cnf={**config_entry_regular})
    #     self.entry_description = tk.Entry(self, cnf={**config_entry_regular})
    #     button_reset = tk.Button(self, text='Reset', command=self.reset, cnf={**config_button_regular})
    #     button_submit = tk.Button(self, text='Submit', command=self.submit, cnf={**config_button_regular})
    #
    #     label_title.place(relx=0.05, rely=0.05)
    #     label_task_name.place(relx=0.12, rely=0.24)
    #     label_deadline.place(relx=0.12, rely=0.4)
    #     label_description.place(relx=0.12, rely=0.56)
    #     self.entry_task_name.place(relx=0.5, rely=0.24, width=200)
    #     self.entry_deadline.place(relx=0.5, rely=0.4, width=200)
    #     self.entry_description.place(relx=0.5, rely=0.56, width=200)
    #     button_reset.place(relx=0.45, rely=0.85, anchor='e')
    #     button_submit.place(relx=0.55, rely=0.85, anchor='w')
    #
    #     self.entry_task_name.focus()

    def reset(self):
        self.entry_task_name.delete(0, 'end')
        self.entry_deadline.delete(0, 'end')
        self.entry_description.delete(0, 'end')

    def submit(self):
        task_name = self.entry_task_name.get()
        deadline = self.entry_deadline.get()
        description = self.entry_description.get()
        self.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()