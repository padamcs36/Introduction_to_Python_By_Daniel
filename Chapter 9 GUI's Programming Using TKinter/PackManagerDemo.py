from tkinter import *
class PackManager:
    def __init__(self):
        root = Tk()
        root.title("Pack Manager Demo")
        root.geometry("300x300")

        Label(root, text='Blue', bg='blue').pack()
        Label(root, text='Red', bg='red').pack(fill=BOTH, expand=1)
        Label(root, text='Green', bg='green').pack(fill=X)

        root.mainloop()
PackManager()