'''
Name: Justin Theyskens
netID: jtheyskens
Student ID: 109558084
'''

import tkinter
from tkinter import *

root = Tk()
root.geometry("320x360")
root.title("Calculator")
root.configure(bg = "white")



def insert_num(text):
    display.configure(state='normal')
    display.insert(END, text)
    display.configure(state='readonly')

def clear_display():
    display.configure(state='normal')
    display.delete(0, END)
    display.configure(state='readonly')

def backspace():
    display.configure(state='normal')
    display.delete(len(display.get())-1, END)
    display.configure(state='readonly')

def calculate():
    try:
        display.configure(state='normal')
        result = eval(display.get())
        display.delete(0,END)
        display.insert(0,result)
        display.configure(state='readonly')
    except:
        display.configure(state='normal')
        display.delete(0, END)
        display.insert(0, "ERROR")
        display.configure(state='readonly')

display = tkinter.Entry(root, width=25, justify='right', font=("Times", 12), state='readonly')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

nine = Button(root, font=("Times", 20), text="9", bg="white", command=lambda: insert_num("9")).grid(row=1,column=3)
eight = Button(root, font=("Times", 20), text="8", bg="white", command=lambda: insert_num("8")).grid(row=1,column=2)
seven = Button(root, font=("Times", 20), text="7", bg="white", command=lambda: insert_num("7")).grid(row=1,column=1)

six = Button(root, font=("Times", 20), text="6", bg="white", command=lambda: insert_num("6")).grid(row=2,column=3)
five = Button(root, font=("Times", 20), text="5", bg="white", command=lambda: insert_num("5")).grid(row=2,column=2)
four = Button(root, font=("Times", 20), text="4", bg="white", command=lambda: insert_num("4")).grid(row=2,column=1)


three = Button(root, font=("Times", 20), text="3", bg="white", command=lambda: insert_num("3")).grid(row=3,column=3)
two = Button(root, font=("Times", 20), text="2", bg="white", command=lambda: insert_num("2")).grid(row=3,column=2)
one = Button(root, font=("Times", 20), text="1", bg="white", command=lambda: insert_num("1")).grid(row=3,column=1)


zero = Button(root, font=("Times", 20), text="0", bg="white", command=lambda: insert_num("0")).grid(row=4,column=1)
left_paren = Button(root, font=("Times", 20), text="(", bg="white", command=lambda: insert_num("(")).grid(row=4,column=2)
right_paren = Button(root, font=("Times", 20), text=")", bg="white", command=lambda: insert_num(")")).grid(row=4,column=3)

plus = Button(root, font=("Times", 20), text="+", bg="white", command=lambda: insert_num("+")).grid(row=5,column=1)
minus = Button(root, font=("Times", 20), text="-", bg="white", command=lambda: insert_num("-")).grid(row=5,column=2)
multi = Button(root, font=("Times", 20), text="*", bg="white", command=lambda: insert_num("*")).grid(row=5,column=3)
divide = Button(root, font=("Times", 20), text="/", bg="white", command=lambda: insert_num("/")).grid(row=5,column=4)

back = Button(root, font=("Times", 14), text="BACK", bg="white", command=backspace).grid(row=1,column=4)
clear = Button(root, font=("Times", 14), text="CLEAR", bg="white", command=clear_display).grid(row=2,column=4)
equals = Button(root, font=("Times", 20), text="=", bg="white", command=calculate).grid(row=4,column=4)

root.mainloop()