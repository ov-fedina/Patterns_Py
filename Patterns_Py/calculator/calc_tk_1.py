from tkinter import * # Import the library
from tkinter import messagebox # Messagebox module - standard dialog box
from tkinter import ttk # ttk module containing more stylized and modern widget classes
import math # We need the math module for mathematical operations
import sys # The python sys module provides functions and variables that are used to control various parts of the Python runtime environment.
# This allows access to system parameters and functions.

window = Tk() # Create a new window
window.title("Calculator") # Add window title

# Create a list with the names of future calculator buttons
bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", ]


# Creating buttons for calculator
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(window, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

# Create an input field
calc_entry = Entry(window, width = 33) # In Python Tkinter, the input field is called Entry, and, for example, in Java Script it is called input.
calc_entry.grid(row=0, column=0, columnspan=5)

#Calculator logic
def calc(key):
    global memory
    if key == "=":

#Exclusion of spelling words
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

#Calculus
# We use the eval function - this is, if I may say so, a compiler within a compiler. It will count in our program.
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

#Clear input field
    elif key == "C":
        calc_entry.delete(0, END)

# Create a function to change minus to plus
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

# The next function is the number pi
    elif key == "π":
        calc_entry.insert(END, math.pi)

# Program exit function
    elif key == "Exit":
        window.after(1,window.destroy)
        sys.exit

# The exponentiation function
    elif key == "xⁿ":
        calc_entry.insert(END, "**")

# When you press the sin or cos key, you get the sine or cosine of the given number
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

# The next two functions are brackets ) and (
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

# A function to get the factorial from a given number
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

# The function of extracting the square root of a given number
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))

# The function that is responsible for clearing the input field when clicking on the "=" button
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# This is "closing" the tkinter window
window.mainloop() # Run an infinite window loop

