from tkinter import *
class ScrollBar:
    def __init__(self):
        tk = Tk()
        tk.title("Scroll Bar")

        frame1 = Frame(tk)
        frame1.pack()
        scrollBr = Scrollbar(frame1)
        scrollBr.pack(side=RIGHT, fill=Y)

        text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollBr.set)
        text.pack()

        scrollBr.config(command=text.yview)

        tk.mainloop()
ScrollBar()