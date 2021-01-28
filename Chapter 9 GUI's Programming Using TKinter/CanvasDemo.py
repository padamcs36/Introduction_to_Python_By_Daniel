from tkinter import *
class CanvasDemo:
    def __init__(self):
        root  = Tk()
        root.title('Canvas Demo')

        self.canvas = Canvas(root, width = 200, height = 200, bg = 'white')
        self.canvas.pack()

        frame = Frame(root)
        frame.pack()

        btRectangle = Button(frame, text='Rectangle', command=self.displayRec)
        btOval = Button(frame, text='Oval', command=self.displayOval)
        btArc = Button(frame, text='Arc', command=self.displayArc)
        btPolygon = Button(frame, text='Polygon', command=self.displayPoly)
        btLine = Button(frame, text='Line', command=self.displayLine)
        btString = Button(frame, text='String', command=self.displayString)
        btClear = Button(frame, text='Clear', command=self.displayClear)

        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btArc.grid(row=1, column=3)
        btPolygon.grid(row=1, column=4)
        btLine.grid(row=1, column=5)
        btString.grid(row=1, column=6)
        btClear.grid(row=1, column=7)

        root.mainloop()

    def displayRec(self):
        self.canvas.create_rectangle(10, 10, 190, 190, tags='Rect')

    def displayOval(self):
        self.canvas.create_oval(10, 10, 170, 190, tags='Oval', fill='red')

    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 190, start=0, extent=90, width=8, tags='Arc', fill='pink')

    def displayPoly(self):
        self.canvas.create_polygon(10, 10, 190, 190, 80, 190, tags='Polygon')

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 190, fill='red', tags='Line')

    def  displayString(self):
        self.canvas.create_text(60, 40, text='Hi, I"m Python Programmer ', tags='text')

    def displayClear(self):
        self.canvas.delete('Rect', 'Oval', 'Arc', 'Polygon', 'Line', 'text')
CanvasDemo()