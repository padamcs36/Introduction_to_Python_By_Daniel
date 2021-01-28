from tkinter import *
class LogIn:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("350x200")
        self.root.title("Login Page")

        Label(self.root, text="Username", font='times 12 italic', padx=10).grid(row=0, column=0,pady=10)
        self.entryName = StringVar()
        Entry(self.root, textvariable=self.entryName).grid(row=0, column=1)

        Label(self.root, text='Password', font='times 12 italic', padx=10).grid(row=1,  column=0)
        self.entryPass = StringVar()
        Entry(self.root, textvariable=self.entryPass).grid(row=1, column=1)

        Button(self.root, text='Login', font='times 12 italic', relief=GROOVE, padx=25, command=self.login).grid(row=2, column=0,padx=25)
        Button(self.root, text='Reset', font='times 12 italic', relief=GROOVE, padx=25, command=self.reset).grid(row=2, column=1)

        self.root.mainloop()

    def login(self):
        if self.entryName.get() == 'Padam Rai' and self.entryPass.get() == 'Motiani':
            print("You login Successfully.")
            Label(self.root, text='You Login Successfully!').grid(row=3, column=1)
        else:
            Label(self.root, text='Username/Password Incorrect!').grid(row=3, column=1)

    def reset(self):
        self.entryPass.set('')
        self.entryName.set('')


LogIn()
