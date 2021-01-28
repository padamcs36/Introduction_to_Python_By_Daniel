from tkinter import *
class WidgetDemo:
    def __init__(self):
        tk = Tk()
        tk.title("widget Demo")

        frame1 = Frame(tk)
        frame1.pack()

        #initializing int variable
        self.v1 = IntVar()
        self.v2 = IntVar()

        ckbtBold = Checkbutton(frame1, text="Bold", variable = self.v1, command=self.processCheckButton)

        rbRed = Radiobutton(frame1, text="Red", bg='red', variable=self.v2, value=1,
                            command=self.processRadioButton)
        rbYellow = Radiobutton(frame1, text="Yellow",bg="yellow", variable=self.v2, value=2,
                               command=self.processRadioButton)

        ckbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        frame2 = Frame(tk)
        frame2.pack()

        label  = Label(frame2, text="enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text="Get name", command=self.getName)
        message = Message(frame2, text="It is a widget Demo")

        label.grid(row=2, column=1)
        entryName.grid(row=2, column=2)
        btGetName.grid(row=2, column = 3)
        message.grid(row=3, column=4)

        text = Text(tk)
        text.pack()
        text.insert(END, "Tip\nThe best way to learn tkinter is to read")
        text.insert(END," these carefully designed examples and use them")
        text.insert(END," to creat your application")


        tk.mainloop()

    def processCheckButton(self):
        print("Check button is checked" if self.v1.get() == 1 else "Unchecked")

    def processRadioButton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected")

    def getName(self):
        print("Your name is ",self.name.get())

WidgetDemo()