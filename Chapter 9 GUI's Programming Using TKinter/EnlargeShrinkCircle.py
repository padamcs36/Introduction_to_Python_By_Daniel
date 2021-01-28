from tkinter  import *
class EnlargeShrink:
    def __init__(self):
        self.radius = 50

        root = Tk()
        root.title("Shrink and Enlarge Circle")
        self.canvas = Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack()

        self.canvas.create_oval(100 - self.radius, 100 - self.radius,
                                100 + self.radius, 100 + self.radius, tags='oval')
        #Bind canvas with mouse events
        #widget.bind(Event, Handler)
        self.canvas.bind("<Button-1>", self.increaseCircle) #left mouse click
        self.canvas.bind("<Button-3>", self.decreaseCircle) #right mouse click

        root.mainloop()
    def increaseCircle(self, event):
        self.canvas.delete('oval') #every single click, it delets the previous circle
        if self.radius < 100:
            self.radius += 2
        self.canvas.create_oval(100 - self.radius, 100 - self.radius,
                                100 + self.radius, 100 + self.radius, tags='oval')
    def decreaseCircle(self, event):
        self.canvas.delete('oval')
        if self.radius > 2:
            self.radius -= 2
        self.canvas.create_oval(100 - self.radius, 100 - self.radius,
                                100 + self.radius, 100 + self.radius, tags='oval')


EnlargeShrink()
