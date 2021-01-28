from tkinter import *
class LabelDemo:
    def __init__(self):
        tk = Tk()
        tk.title("Change Label Demo")

        frame1 = Frame(tk)
        frame1.pack()
        self.lbl = Label(frame1, text='Programming is fun')
        self.lbl.pack()

        # Add a label, entry, button, two radio buttons to frame2
        frame2 = Frame(tk)
        frame2.pack()

        label = Label(frame2, text='Enter text')

        self.message = StringVar()
        entry = Entry(frame2, textvariable = self.message)
        bttxtChange = Button(frame2, text='Change text', command= self.processButton)

        self.v1 = StringVar()
        btred = Radiobutton(frame2, text='Red', bg='Red', variable=self.v1, value = 'R',
                            command=self.processRadioButton)
        btyellow = Radiobutton(frame2, text='Yellow', bg='yellow', variable=self.v1, value='Y',
                               command=self.processRadioButton)
        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        bttxtChange.grid(row=1, column=3)
        btred.grid(row=1, column=4)
        btyellow.grid(row=1, column=5)

        tk.mainloop()

    def processButton(self):
        self.lbl['text'] = self.message.get()

    def processRadioButton(self):
        if self.v1.get() == 'R':
            self.lbl['fg'] = 'red'
            self.lbl['bg'] = 'gray'
        elif self.v1.get() == 'Y':
            self.lbl['fg'] = 'yellow'
            self.lbl['bg'] = 'magenta'
LabelDemo()