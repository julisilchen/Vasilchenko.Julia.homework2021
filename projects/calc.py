import tkinter as tk

window = tk.Tk()
# Название окна
# Размеры
# Неизменяемость
# Фон
window.title('Калькулятор')
window.geometry('500x550')
window.resizable(False, False)
window.configure(bg='#c197e8')
window.iconphoto(False, tk.PhotoImage(file = 'calculator.png'))


# Функция высчитывания операций калькулятора
def calculate(operation):
    global formula

    if operation =='C':
        formula = ''
    elif operation == '=':
        formula = str(eval(formula))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


# Создание окнв для вывода вычислений
formula = '0'
label_text = tk.Label(text=formula, font=('Roboto', 30, 'bold'), bg='#c197e8', fg='white')
label_text.place(x=11, y=50)


# Создание кнопок
buttons = ['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '/', '0', 'C', '=']
x = 18
y = 210
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg='#A168D5', fg='white', font=('Roboto', 20), command= get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x> 400:
        x = 18
        y += 81

window.mainloop()