from tkinter import *
class FutureInvestment:
    def __init__(self):
        tk = Tk()
        tk.title("Futrue Investment")
        tk.geometry("250x200")


        Label(tk, text='Investment Amount').grid(row=1, column=1, sticky=W, pady=5)
        Label(tk, text='Years').grid(row=2, column=1, sticky=W, pady=5)
        Label(tk, text='Anual Interest Rate').grid(row=3, column=1, sticky=W, pady=5)
        Label(tk, text='Future Value').grid(row=4, column=1, sticky=W, pady=5)

        self.InvestmentAmount = StringVar()
        Entry(tk, textvariable=self.InvestmentAmount, justify=RIGHT).grid(row=1, column=2)

        self.years = StringVar()
        Entry(tk, textvariable=self.years, justify=RIGHT).grid(row=2, column=2)

        self.AnualInterestRate = StringVar()
        Entry(tk, textvariable=self.AnualInterestRate, justify=RIGHT).grid(row=3, column=2)

        self.futureValue = StringVar()
        Entry(tk,  textvariable=self.futureValue, justify=RIGHT).grid(row=4, column=2)

        Button(tk, text="Calculate", command=self.computeFutureValue, relief=SOLID).grid(row=5, column=2, sticky=E)

        tk.mainloop()

    def computeFutureValue(self):
        monthlyInterestRate = float(self.AnualInterestRate.get()) / 1200
        futureValue = float(self.InvestmentAmount.get()) * (1 + monthlyInterestRate) ** (float(self.years.get()) * 12)
        return self.futureValue.set(format(futureValue, "10.2f"))
FutureInvestment()