from tkinter import *
from tkinter import messagebox
from numpy.polynomial import Polynomial as P


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()


def findroots1():
    function = coefficientsInput1.get()
    l = list(map(int, function.split(' ')))
    l.reverse()
    p = P(l)
    info_str = f'Ваше уровнение: {str(p)}'
    messagebox.showinfo(title='Ваше уровнение', message=info_str.replace('**', '^'))
    info_str = f'Корни: {str(p.roots())}'
    messagebox.showinfo(message=info_str)


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Мое приложение")

tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=400, height=400)
canvas.pack()

frame = Frame(tk, bg="white")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
title = Label(frame, text='Введите коэфиценты уравнение', bg="white")
title.pack()
coefficientsInput1 = Entry(frame, bg='white')
coefficientsInput1.place(y=125)
coefficientsInput1.pack()
b0 = Button(tk, text="Найти корни уровнения", command=findroots1)
b0.place(x=130, y=125)


tk.mainloop()
