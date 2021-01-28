from tkinter import *
class CheckerBoard:
    def __init__(self):
        tk = Tk()
        tk.title('CheckerBoard')
        # tk.geometry('250x250')

        canvas = Canvas(tk, width=250, height=250, bg='white')
        canvas.pack()
        dx=12
        canvas.create_rectangle(10, 10, 30, 30, fill='white',tags='rect')
        for i in range(8):
            for i in range(8):
                canvas.move('tags', dx, 0)
                if i % 2 == 0:
                    canvas.create_rectangle(10,10,30,30, fill='white')
                else:
                    canvas.create_rectangle(10,10,30,30, fill='black')
            canvas.after(50)
            canvas.update()

        tk.mainloop()
CheckerBoard()