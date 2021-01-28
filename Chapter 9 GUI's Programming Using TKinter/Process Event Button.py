from tkinter import *
import sys
tk = Tk()
def processOk():
    print("Ok Button is clicked")
def processCancel():
    print("Cancel Button is clicked")
    sys.exit()

btOk = Button(tk, text="OK", fg="red", command=processOk)
btCancel = Button(tk, text="Cancel", bg="yellow", command=processCancel)

btOk.pack()
btCancel.pack()

tk.mainloop()