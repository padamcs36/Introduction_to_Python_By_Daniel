from tkinter import *
import sys
class ProcessButton:
    def __init__(self):
        tk = Tk()

        btOk = Button(tk, text="Ok", command=self.Ok,
                      font='Courier 20 bold italic overstrike underline')
        btCancel = Button(tk,  text="Cancel", command=self.cancel, font='Times 10 bold',
                          justify=LEFT, fg='white',bg='black')

        btOk.pack()
        btCancel.pack()

        tk.mainloop()
    def Ok(self):
        print("OK button is clicked")
        sys.exit()

    def cancel(self):
        print("Cancel Button is clicked.")
        sys.exit()

ProcessButton()