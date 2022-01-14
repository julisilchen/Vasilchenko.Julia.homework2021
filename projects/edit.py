from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('Заметки')
root.geometry('500x530')
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file = 'edit.png'))

main_menu = Menu(root)


def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']


def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы(*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path,encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы(*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()


# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт', menu=font_menu_sub)
root.config(menu=view_menu)


# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# Словарь
view_colors = {
    'light': {
        'text_bg': '#d5bbed', 'text_fg': 'black', 'cursor': '#e600a1', 'select_bg': '#8E41D5'
    },
    'dark': {
        'text_bg': 'black', 'text_fg': '#e600a1', 'cursor': 'white', 'select_bg': '#80917A'
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 12 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 12, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 12, 'bold')
    }
}

# Главные свойства
text_fild = Text(f_text,
                 bg='#d5bbed',
                 fg='black',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='#e600a1',
                 selectbackground='#8E41D5',
                 spacing3=10,
                 width=30,
                 font= 'Arial 12 bold'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)


root.mainloop()