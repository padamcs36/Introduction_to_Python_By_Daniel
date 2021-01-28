from tkinter import *
class DisplayRect:
    def __init__(self):
        tk = Tk()
        tk.title("Display 20 Rectangle")
        self.x = 5
        self.y = 5
        self.canvas = Canvas(tk, width=400, height=300, bg='white')
        self.canvas.pack()

        # while self.x < 10 and self.y < 10:
        #     self.canvas.create_rectangle(10 + self.x, 10+self.y ,190 - self.x,190 - self.y)
        #     self.x += 2
        #     self.y += 2

        for i in range(20):
            self.canvas.create_rectangle(10 + i * 6, 10 + i * 6,
                int(self.canvas["width"]) - 10 - i * 6, int(self.canvas["height"]) - 10 - i * 6)


        tk.mainloop()
DisplayRect()