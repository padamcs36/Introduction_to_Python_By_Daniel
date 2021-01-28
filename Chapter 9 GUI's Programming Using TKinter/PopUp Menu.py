from tkinter import *
class PopUpMenu:
    def __init__(self):
        root = Tk()
        root.title('PopUp Menu')

        self.menu = Menu(root, tearoff = 0)
        root.config(menu=self.menu)
        self.menu.add_command(label='Draw a line', command=self.displayLine)
        self.menu.add_command(label='Draw a Oval', command=self.displayOval)
        self.menu.add_command(label='Draw a Rectangle', command=self.displayRect)
        self.menu.add_command(label='Clear', command=self.displayClear)

        self.canvas = Canvas(root, width=300, height=200, bg='white')
        self.canvas.pack()

        #Bind popup to canvas
        self.canvas.bind("<Button-3>", self.popup)

        root.mainloop()

    def displayLine(self):
        self.canvas.create_line(10,10,190,190, tags='line')
    def displayOval(self):
        self.canvas.create_oval(10,10,190,190, tags='oval')
    def displayRect(self):
        self.canvas.create_rectangle(10,10,190,190, tags='rect')

    def displayClear(self):
        self.canvas.delete('line', 'oval', 'rect')

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

PopUpMenu()