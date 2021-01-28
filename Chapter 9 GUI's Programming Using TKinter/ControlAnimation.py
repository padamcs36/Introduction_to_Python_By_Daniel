from tkinter import *
class ControlAnimation:
    def __init__(self):
        root = Tk()
        root.title("Control Animation")

        self.width = 250
        self.canvas = Canvas(root, width=self.width,  height=100, bg='white')
        self.canvas.pack()

        frame = Frame(root)
        frame.pack()

        btStop = Button(frame, text="Stop", command=self.stop)
        btStop.pack(side=LEFT)

        btResume = Button(frame, text='Resume', command=self.resume)
        btResume.pack(side=LEFT)

        btFaster = Button(frame, text="Faster", command=self.faster)
        btFaster.pack(side=LEFT)

        btSlower = Button(frame, text='Slower', command=self.slower)
        btSlower.pack(side=LEFT)

        self.x = 0
        self.sleepTime = 100
        self.canvas.create_text(self.x, 30, text='message moving', tags='txt')
        # self.canvas.create_oval(self.x, 0, 30,30, tags='txt', fill='red')

        self.dx = 3
        self.isStopped = False
        self.animate()

        root.mainloop()

    def stop(self):
        self.isStopped = True

    def resume(self):
        self.isStopped = False
        self.animate()

    def faster(self):
        if self.sleepTime > 5:
            self.sleepTime -= 20

    def slower(self):
        self.sleepTime += 20

    def animate(self):
        while not self.isStopped: #isStopped is True then terminate the Loop
            self.canvas.move('txt', self.dx, 0)
            self.canvas.after(self.sleepTime)
            self.canvas.update()

            if self.x < self.width:
                self.x += self.dx
            else:
                self.x = 0
                self.canvas.delete('txt')
                self.canvas.create_text(self.x, 30, text='message moving', tags='txt')
                # self.canvas.create_oval(self.x, 0, 30, 30, tags='txt', fill='red')


ControlAnimation()