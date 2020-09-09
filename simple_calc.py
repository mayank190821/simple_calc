# simple calc
from tkinter import *

root = Tk()
root.title("Calculator")
# window size
root.geometry('380x348')
take_input = Entry(root, text="Enter digits", fg="Black", borderwidth=5, width=45)
take_input.grid(row=0, column=0, columnspan=3)
take_input.insert(0, "0")


def click(num):
    take_input.delete(0, END)
    current_number = take_input.get()
    take_input.delete(0, END)
    take_input.insert(0, str(current_number) + str(num))


def clear():
    take_input.delete(0, END)


def add():
    global num1
    global task
    task = "add"
    num1 = int(take_input.get())
    take_input.delete(0, END)


def equal():
    global num2
    number2 = take_input.get()
    num2 = number2
    take_input.delete(0, END)
    if task == "add":
        take_input.insert(0, num1 + int(num2))
    if task == "subtract":
        take_input.insert(0, num1 - int(num2))
    if task == "multiply":
        take_input.insert(0, num1 * int(num2))
    if task == "divide":
        take_input.insert(0, num1 / int(num2))


def subtract():
    global num1
    global task
    task = "subtract"
    num1 = int(take_input.get())
    take_input.delete(0, END)


def multiply():
    global num1
    global task
    task = "multiply"
    num1 = int(take_input.get())
    take_input.delete(0, END)


def divide():
    global num1
    global task
    task = "divide"
    num1 = int(take_input.get())
    take_input.delete(0, END)


# defining buttons
button_1 = Button(root, text="1", command=lambda: click(1), padx=40, pady=20)
button_2 = Button(root, text="2", command=lambda: click(2), padx=40, pady=20)
button_3 = Button(root, text="3", command=lambda: click(3), padx=40, pady=20)
button_4 = Button(root, text="4", command=lambda: click(4), padx=40, pady=20)
button_5 = Button(root, text="5", command=lambda: click(5), padx=40, pady=20)
button_6 = Button(root, text="6", command=lambda: click(6), padx=40, pady=20)
button_7 = Button(root, text="7", command=lambda: click(7), padx=40, pady=20)
button_8 = Button(root, text="8", command=lambda: click(8), padx=40, pady=20)
button_9 = Button(root, text="9", command=lambda: click(9), padx=40, pady=20)
button_0 = Button(root, text="0", command=lambda: click(0), padx=40, pady=20)
button_add = Button(root, text="+", command=add, padx=39, pady=52)
button_subtract = Button(root, text="-", command=subtract, padx=39, pady=20)
button_multiply = Button(root, text="*", command=multiply, padx=39, pady=20)
button_divide = Button(root, text="/", command=divide, padx=39, pady=20)
button_clear = Button(root, text="Clear", command=clear, padx=77, pady=20)
button_equal = Button(root, text="=", command=equal, padx=135, pady=20)

# Positioning button
button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)
button_multiply.grid(row=1, column=3)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)
button_subtract.grid(row=2, column=3)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_divide.grid(row=3, column=3)
button_add.grid(rowspan=2, column=3)
button_clear.grid(row=4, column=1, columnspan=2)
button_0.grid(row=4, column=0)

button_equal.grid(row=5, columnspan=3)
root.resizable(0, 0)
root.mainloop()
