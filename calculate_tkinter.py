import tkinter as tak
from tkinter import messagebox
from turtle import clear

def add_button(number):
    value = calc.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:] 
    calc.delete(0, tak.END)
    calc.insert(0, value+number)


def calculation():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc.delete(0, tak.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Недопустимые знаки')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('На ноль делить нельзя')
        calc.insert(0,0)
        
    


def add_operator(operator):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value [:-1]
    calc.delete(0, tak.END)
    calc.insert(0, value+operator)


def clear():
    calc.delete(0, tak.END)
    calc.insert(0, 0)

def made_button(number):
    return tak.Button(text=number, bd=5, font=('TimesNewRoman', 15), 
        command=lambda: add_button (number))
    
def made_operator(operator):
    return tak.Button(text=operator, bd=5, font=('TimesNewRoman', 15), 
        command=lambda: add_operator (operator))

def made_calculation(operator):
    return tak.Button(text=operator, bd=5, font=('TimesNewRoman', 15), 
        command=calculation)

def made_clear(operator):
    return tak.Button(text=operator, bd=5, font=('TimesNewRoman', 15), 
        command=clear)

logotip = tak.Tk()
logotip.geometry(f'240x270+100+200')
logotip['bg'] = '#fff'
logotip.title('Калькулятор')

calc = tak.Entry(logotip, justify= tak.RIGHT, font=('TimesNewRoman', 15), width=17)
calc.insert(0, '0')
calc.grid(row = 0, column=0, columnspan= 4, stick='we', padx=5)

made_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
made_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
made_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
made_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
made_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
made_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
made_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
made_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
made_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)   
made_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

made_operator('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
made_operator('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
made_operator('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
made_operator('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

made_calculation('=').grid(row=4, column=1, stick='wens', padx=5, pady=5)

made_clear('<<').grid(row=4, column=2, stick='wens', padx=5, pady=5)


logotip.grid_columnconfigure(0, minsize= 60)
logotip.grid_columnconfigure(1, minsize= 60)
logotip.grid_columnconfigure(2, minsize= 60)
logotip.grid_columnconfigure(3, minsize= 50)

logotip.grid_rowconfigure(1, minsize= 60)
logotip.grid_rowconfigure(2, minsize= 60)
logotip.grid_rowconfigure(3, minsize= 60)
logotip.grid_rowconfigure(4, minsize= 60)

if __name__ == '__main__':
    logotip.mainloop()
