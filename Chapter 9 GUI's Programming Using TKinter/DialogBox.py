import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

# tkinter.messagebox.showinfo("showinfo", "This is an info message") #first arguement title and seccod message
# tkinter.messagebox.showwarning("showwarning", "This is a warning")
# tkinter.messagebox.showerror("showerror", "This is an error")
#
# isYes = tkinter.messagebox.askyesno("askyesno", "continue?")
# print(isYes)
#
# isYesNoCancel = tkinter.messagebox.askyesnocancel("askyesnocancel", "Yes, No, Cancel")
# print(isYesNoCancel)
#
# name = tkinter.simpledialog.askstring("askString", "Enter your name ")
# print(name)
#
# age = tkinter.simpledialog.askinteger("askInteger", "Enter your age ")
# print(age)
#
# weight = tkinter.simpledialog.askfloat("askFloat", "Enter your weight")
#
# if name == "Padam" and age == 23:
#     print("You login Successfully.")

tkinter.messagebox.showinfo("ShowInfo", "Welcome to Python")

name = tkinter.simpledialog.askstring("Name", "Enter your name")
age = tkinter.simpledialog.askinteger("Age", "Enter  your age")
weight = tkinter.simpledialog.askfloat("Weight", "Enter your weight")