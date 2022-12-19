from tkinter import messagebox

from numpy.polynomial import Polynomial as P
from tkinter import *

root = Tk()


def findroots():
    function = coefficientsInput.get()
    l = list(map(int, function.split(' ')))
    p = P(l)
    info_str = f'Ваше уровнение: {str(p)}'
    messagebox.showinfo(title='Ваше уровнение', message=info_str)
    info_str = f'Корни: {str(p.roots())}'
    messagebox.showinfo(message=info_str)


root.title('Поиск корней квадратного уровнения')
root.geometry('500x400')
title = Label(root, text='Ввидете уровнение')
title.pack()
coefficientsInput = Entry(root, bg='white')
coefficientsInput.pack()
button = Button(root, text='Найти корни', bg='grey', command=findroots)
button.pack()
root.mainloop()

