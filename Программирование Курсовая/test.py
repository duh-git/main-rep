import tkinter as tk




class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f'{800}x{600}')
        self.resizable(False, False)
        self.config(bg='#10151a')

        self.display()

    def display(self):
        self.add_task__frame = Add(self)
        self.add_task__frame.grid(row=0, column=0, sticky='nswe')
        self.employee_list__frame = Employee(self).grid(row=0, column=1, sticky='nswe')

class Add(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = '#fff'
        self['width'] = 100
        self['height'] = 100
        # self.master['background']


class Employee(tk.Frame):
    def __init__(self, master):
        super().__init__()


if __name__ == '__main__':
    app = App()
    app.mainloop()