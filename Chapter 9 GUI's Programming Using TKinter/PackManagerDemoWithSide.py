from tkinter import *
class PackManager:
    def __init__(self):
        root = Tk()
        root.title("Pack Manager with side by Side")
        # root.geometry("300x300")

        Label(root, text='red', bg='red').pack(side=LEFT)
        Label(root, text='blue', bg='blue').pack(side=RIGHT, fill=BOTH, expand=1)
        Label(root, text='green', bg='green').pack(side=LEFT, fill=BOTH)

        root.mainloop()
PackManager()