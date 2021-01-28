from tkinter import *
class  GeometricFigure:
    def __init__(self):
        tk = Tk()
        tk.title("Goemetric Figure")

        self.canvas = Canvas(tk, width=200, height=100, bg='white')
        self.canvas.pack()
        self.btnCheck = IntVar()

        frame = Frame(tk)
        frame.pack()

        btRect = Radiobutton(frame, text='Recangle', variable=self.btnCheck,command=self.processBtn, value=1)
        btRect.pack(side=LEFT)

        btOval = Radiobutton(frame, text='Oval', variable=self.btnCheck,command=self.processBtn,  value=2)
        btOval.pack(side=LEFT)

        Checkbutton(frame, text='Fill', command=self.btnchecked).pack(side=LEFT)

        tk.mainloop()

    def processBtn(self):
        if self.btnCheck.get() == 1:
            self.canvas.delete('oval')
            self.canvas.create_rectangle(10, 10, 100, 100, tags='rect')

        if self.btnCheck.get() == 2:
            self.canvas.delete('oval')
            self.canvas.create_oval(10, 10, 100, 100, tags='oval')

GeometricFigure()
