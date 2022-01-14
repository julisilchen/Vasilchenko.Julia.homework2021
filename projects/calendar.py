from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Расписание')
root.geometry('600x600')
root.resizable(False, False)
root.configure(bg='#c197e8')
root.iconphoto(False, tk.PhotoImage(file = 'calendar.png'))

main_menu = Menu(root)

buttons = ['Время', 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ',
           '8:45-10:20', 'Прогр.', '', 'Физ-ра', '', '', 'Физика',
           '10:35-12:10', 'История', '',  'Прогр', '',  'Мат.ан.', 'Физика',
           '12:25-14:00', '', 'Лин.ал.', '', 'Англ.яз', 'Физика', '',
           '14:45-16:20', '', '', '', 'Лин.ал.', '', '',
           '16:35-18:10', 'Англ.яз.', 'Мат.ан.', '', '', 'История', '',
           '18:25-20:00', '', '', '', '', '', 'Физ-ра', ]
x = 15
y = 40
for button in buttons:
    tk.Button(text=button,  fg='white', bg='#A168D5', font=('Roboto', 10),).place(x=x, y=y, width=80, height=60)
    x += 82
    if x <= 530:
        continue
    x = 15
    y += 62

button_1 = Button(root,
                  text="Данная страница находится в разработке. Ждите обновления.",
                  height=1,
                  width=40,
                  padx=60,
                  pady=40,
                  bg='#A168D5',
                  fg='red'
                  )
button_1.place(x=15, y=480)

root.mainloop()