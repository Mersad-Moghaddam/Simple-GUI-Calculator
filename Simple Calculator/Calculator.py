from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("370x340")
root.maxsize(370, 340)
root.minsize(370, 340)


# user input
user_input = Entry(root, width=35, borderwidth=5, bg="gray", fg="white")
user_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Function
def button_click(number):
    current = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0, str(current) + str(number))


def button_clear():
    user_input.delete(0, END)


def button_equal():
    second_number = user_input.get()
    global s_num
    s_num = float(second_number)
    user_input.delete(0, END)
    result = 0
    if match == "add":
        result = f_num + s_num
    if match == "sub":
        result = f_num - s_num
    if match == "mul":
        result = f_num * s_num
    if match == "div":
        result = f_num / s_num
    if match == "pow":
        result = f_num ** s_num
    user_input.insert(0, str(result))


def button_add():
    first_number = user_input.get()
    global f_num
    global match
    match = "add"
    f_num = float(first_number)
    user_input.delete(0, END)


def button_sub():
    first_number = user_input.get()
    global f_num
    global match
    match = "sub"
    f_num = float(first_number)
    user_input.delete(0, END)


def button_mul():
    first_number = user_input.get()
    global f_num
    global match
    match = "mul"
    f_num = float(first_number)
    user_input.delete(0, END)


def button_div():
    first_number = user_input.get()
    global f_num
    global match
    match = "div"
    f_num = float(first_number)
    user_input.delete(0, END)

def button_power():
    first_number = user_input.get()
    global f_num
    global match
    match = "pow"
    f_num = float(first_number)
    user_input.delete(0, END)

# define Button
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_00 = Button(root, text="00", padx=16, pady=10, command=lambda: button_click(00))
button_add = Button(root, text="+", padx=19, pady=10, command=button_add)
button_sub = Button(root, text="-", padx=19, pady=10, command=button_sub)
button_mul = Button(root, text="*", padx=21, pady=10, command=button_mul)
button_div = Button(root, text="/", padx=24, pady=10, command=button_div)
button_power = Button(root, text="**", padx=21, pady=10, command=button_power)
button_equal = Button(root, text="=", padx=41, pady=10, command=button_equal)
button_clear = Button(root, text="Clear", padx=35, pady=10, command=button_clear)

# put the button on the Screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_00.grid(row=4, column=2, columnspan=1)

button_equal.grid(row=6, column=0, columnspan=1)
button_add.grid(row=5, column=0, columnspan=1)
button_sub.grid(row=4, column=0, columnspan=1)
button_mul.grid(row=5, column=1, columnspan=1)
button_div.grid(row=5, column=2, columnspan=1)
button_power.grid(row=6, column=2, columnspan=1)
button_clear.grid(row=6, column=1, columnspan=1)
root.mainloop()
