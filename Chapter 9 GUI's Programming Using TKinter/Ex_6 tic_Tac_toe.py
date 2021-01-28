from tkinter import *  # Import tkinter
from random import randint


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Tic Tac Toe")  # Set a title

        # imageX = PhotoImage(file="image/x.gif")
        # imageO = PhotoImage(file="image/o.gif")

        for i in range(3):
            frame = Frame(window)
            frame.pack()
            for j in range(3):
                label = Label(frame, font='lucida 12 bold' ,text='X' if randint(0, 1) == 0 else 'O')
                label.pack(side=LEFT, padx=10)

        window.mainloop()  # Create an event loop

MainGUI()
