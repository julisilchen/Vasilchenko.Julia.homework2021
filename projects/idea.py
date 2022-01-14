from tkinter import *
import tkinter as tk
import os

root = tk.Tk()
root.title('Главная часть')
root.geometry('600x600')
root.resizable(False, False)
root.configure(bg='#c197e8')
root.iconphoto(False, tk.PhotoImage(file = 'idea.png'))

main_menu = Menu(root)


def btnClickFunctionA():
   import calendar
   os.system(open(calendar))


def btnClickFunctionB():
    import calc
    os.system(open(calc))


def btnClickFunctionC():
    import edit
    os.system(open(edit))


button_1 = Button(root,
                  text="Расписание",
                  height=1,
                  width=10,
                  padx=60,
                  pady=20,
                  bg='#A168D5',
                  fg='white',
                  command=lambda: btnClickFunctionA())
button_1.place(x=210, y=200)

button_2 = Button(root,
                  text="Калькулятор",
                  height=1,
                  width=10,
                  padx=60,
                  pady=20,
                  bg='#A168D5',
                  fg='white',
                  command=lambda: btnClickFunctionB())
button_2.place(x=210, y=280)

button_3 = Button(root,
                  text="Заметки",
                  height=1,
                  width=10,
                  padx=60,
                  pady=20,
                  bg='#A168D5',
                  fg='white',
                  command=lambda: btnClickFunctionC())
button_3.place(x=210, y=360)

root.mainloop()