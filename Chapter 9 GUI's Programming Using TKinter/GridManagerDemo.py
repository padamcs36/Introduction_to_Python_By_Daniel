#padx and pady is used to space the horizontal and vertical space outside the widgets
#ipadx  and ipady is used to space the  horizontal and vertical space inside the widgets.

from tkinter import *
class GridManager:
    def __init__(self):
        self.root = Tk()
        self.root.title("Grid Manager")
        self.root.geometry("300x150")

        message = Message(self.root, text='This message grid occupy three row and two columns')
        message.grid(row=1, column=1, rowspan=3, columnspan=2)

        self.fName = StringVar()
        self.lName = StringVar()

        Label(self.root, text='First Name').grid(row=1, column=3)
        Fname = Entry(self.root, textvariable=self.fName)
        Fname.grid(row=1, column=4, padx=5, pady=5)

        Label(self.root, text='Last Name').grid(row=2, column=3)
        Lname = Entry(self.root, textvariable=self.lName)
        Lname.grid(row=2, column=4)

        Button(self.root, text='Get Name', command=self.getName, relief = GROOVE).grid(row=3, column=4, padx=5, pady=5, ipadx=30, sticky=E)

        self.root.mainloop()

    def getName(self):
        Label(self.root, text = self.fName.get() +" "+ self.lName.get()).grid(row=4, column=3)
GridManager()