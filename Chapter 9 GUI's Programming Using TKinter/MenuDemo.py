from tkinter import *
class SimpleCalculator:
    def  __init__(self):
        root = Tk()
        root.title('Simple Calculator')

        mainMenu = Menu(root)
        root.config(menu = mainMenu) #Display the menu bar.

        # Create a pull-down menu, and add it to the menu bar
        OperationSubMenu = Menu(mainMenu, tearoff=0)
        mainMenu.add_cascade(label='Operation', menu=OperationSubMenu)
        OperationSubMenu.add_command(label='Add', command=self.add)
        OperationSubMenu.add_command(label='Mul', command=self.mul)
        OperationSubMenu.add_separator()
        OperationSubMenu.add_command(label='Sub', command=self.sub)
        OperationSubMenu.add_command(label='Div', command=self.div)

        exitMenu = Menu(mainMenu, tearoff=0)
        mainMenu.add_cascade(label='Exit', menu=exitMenu)
        exitMenu.add_command(label='Quit', command=root.quit)

        # frame0 = Frame(root)
        # frame0.grid(row=1, column=1, sticky=W)
        #
        # Button(frame0, text='+', font='times 15 bold', command=self.add).grid(row=1, column=1, sticky=W,ipadx=10)
        # Button(frame0, text='-', font='times 15 bold', command=self.sub).grid(row=1, column=2,ipadx=10)
        # Button(frame0, text='x', font='times 15 bold', command=self.mul).grid(row=1, column=3,ipadx=10)
        # Button(frame0, text='/', font='times 15 bold', command=self.div).grid(row=1, column=4,ipadx=10)

        frame1 = Frame(root)
        frame1.grid(row=2, column=1, pady=10)

        Label(frame1, text='Num-1').pack(side=LEFT)
        self.v1 = StringVar()
        Entry(frame1, textvariable=self.v1, justify=RIGHT).pack(side=LEFT)

        Label(frame1, text='Num-2').pack(side=LEFT)
        self.v2 = StringVar()
        Entry(frame1, textvariable=self.v2, justify=RIGHT).pack(side=LEFT)

        Label(frame1, text='Result').pack(side=LEFT)
        self.v3 = StringVar()
        Entry(frame1, textvariable=self.v3, justify=RIGHT, width=10).pack(side=LEFT)

        frame2 = Frame(root)
        frame2.grid(row=3, column=1, pady=10)

        Button(frame2, text='Add', command=self.add).pack(side=LEFT)
        Button(frame2, text='Sub', command=self.sub).pack(side=LEFT)
        Button(frame2, text='Mul', command=self.mul).pack(side=LEFT)
        Button(frame2, text='Div', command=self.div).pack(side=LEFT)

        mainloop()

    def add(self):
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
    def sub(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
    def mul(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
    def div(self):
        self.v3.set(eval(self.v1.get()) /  eval(self.v2.get()))

SimpleCalculator()