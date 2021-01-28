#Todo: TKINTER GUI
import random
lottery = random.randint(0, 99)
# guess = eval(input("Enter your lottery guess pick(two digits): "))
def getGuess():
    lotteryDigit1 = lottery // 10
    lotteryDigit2 = lottery % 10

    guess = guessEntry.get()
    guessDigit1 = int(guess) // 10
    guessDigit2 = int(guess) % 10

    if lottery == int(guess):
        return Label(frame, text="Exact match, You win $10000", relief=GROOVE, fg='red', bg='yellow',
                     font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)

    elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
        return Label(frame, text="All match, You win $3000", relief=GROOVE, fg='White', bg='yellow',
                     font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)

    elif (guessDigit1 == lotteryDigit1 or
         guessDigit1 == lotteryDigit2 or
        guessDigit2 == lotteryDigit1 or
        guessDigit2 == lotteryDigit2):
        return Label(frame, text="One digit Match, You win $1000", relief=GROOVE, fg='blue', bg='yellow',
                     font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)

    else:
        return Label(frame, text="Sorry, No digit Match.", relief=GROOVE, fg='red', bg='yellow',
                     font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)

from tkinter import *
root = Tk()
root.title("Lottery")
root.geometry("400x400")

frame = Frame(root, relief=RIDGE)
frame.place(x=80,y=10, width=500, height=400)
label = Label(frame, text='LOTTERY GAME', relief=GROOVE, fg='red', bg='yellow', font=('time new roman',14,'bold'))
label.grid(row=0, column=2, pady=25)

rollLabel = Label(frame, text='Guess Num:', font=('time new roman', 12, 'bold'), bg='crimson',fg='white')
rollLabel.grid(row=1, column=2,pady=20,padx=55,sticky='w')

guessEntry = StringVar()
rollEntry = Entry(frame,textvariable=guessEntry ,font=('time new roman', 15, 'bold'), bd=5, relief=GROOVE)
rollEntry.grid(row=2, column=2,pady=20, sticky='w')

btnGuess = Button(frame, text='Guess', width=15, font=('time new roman', 12, 'bold'), command=getGuess)
btnGuess.grid(row=3, column=2, pady=20, padx=38, sticky='w')

root.mainloop()
