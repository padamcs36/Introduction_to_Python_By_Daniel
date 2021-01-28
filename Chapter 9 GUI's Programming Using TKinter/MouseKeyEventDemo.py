from tkinter import *
class MouseKeyEvent:
    def __init__(self):
        root  = Tk()
        root.title('Mouse Key Event')

        canvas = Canvas(root, width=200, height=200, bg='white')
        canvas.pack()

        #Bind with <Button-1> event => Left touchpad button
        canvas.bind("<Button-1>", self.processMouseEvent)

        #Bind with <key> event
        canvas.bind("<Key>", self.processKeyEvent)
        canvas.focus_set()

        root.mainloop()
    def processMouseEvent(self, event):
        print("Clicked at ", event.x, event.y)
        print("Position in the screen ", event.x_root, event.y_root)
        print("Which Button is clicked ", event.num)

    def processKeyEvent(self, event):
        print("Keysym ? ", event.keysym)
        print("Char ? ", event.char)
        print("Keycode ? ", event.keycode)
MouseKeyEvent()