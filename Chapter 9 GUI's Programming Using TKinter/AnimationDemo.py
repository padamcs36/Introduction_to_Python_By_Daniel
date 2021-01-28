from tkinter import *
class AnimationDemo:
    def __init__(self):
        root = Tk()
        root.title("Animation")
        width = 250

        canvas = Canvas(root, width = 250, height=50, bg='white')
        canvas.pack()

        x = 0 #starting x position
        canvas.create_text(x, 30, text='Message Moving?', tags="txt")

        dx = 3
        while True:
            canvas.move("txt", dx, 0) #Move text dx unit
            canvas.after(100) #sleep after 100 milliseconds
            canvas.update() #upadate canvas

            if x < width:
                x += dx #Get the current position for the string

            else:
                x = 0  # Reset string position to the beginning
                canvas.delete("txt")
                # Redraw text at the beginning
                canvas.create_text(x, 30, text='Message Moving?', tags="txt")

            root.mainloop()
AnimationDemo()

