from tkinter import *
class MovingBall:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Moving Ball")

        canvas = Canvas(self.tk, width=400, height=200, bg='lightgray')
        canvas.pack()

        ball = canvas.create_oval(10, 10, 30, 30, fill='orange', tags='dot')
        xspeed = 10
        yspeed = 8

        while True:
            canvas.move(ball, xspeed, yspeed)
            pos = canvas.coords(ball)
            if pos[3] >= 200 or pos[1] <= 0:
                yspeed = -yspeed
            if pos[2] >= 400 or pos[0] <= 0:
                xspeed = -xspeed
            canvas.after(50)
            self.tk.update()

MovingBall()

