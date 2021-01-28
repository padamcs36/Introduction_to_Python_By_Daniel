from tkinter import *
class LoanCalculator:
    def __init__(self):
        root = Tk()
        root.title("Loan Calculator")
        root.geometry("250x250")
        root.maxsize(width=300, height=250)
        # Label(root, text='Annual Tax System', font='lucida 12 italic',justify=CENTER).grid(row=0, column=2)
        Label(root, text='Annual Interest Rate').grid(row=1, column=1, sticky=W, pady=5)
        Label(root, text='Number of Years').grid(row=2, column=1, sticky=W, pady=5)
        Label(root, text='Loan Amount').grid(row=3, column=1, sticky=W, pady=5)
        Label(root, text='Monthly Payment').grid(row=4, column=1, sticky=W, pady=5)
        Label(root, text='Total payment').grid(row=5, column=1, sticky=W, pady=5)

        self.annualInterestRate = StringVar()
        Entry(root, textvariable=self.annualInterestRate, justify=RIGHT).grid(row=1, column=2)

        self.numberOfYear = StringVar()
        Entry(root, textvariable=self.numberOfYear, justify=RIGHT).grid(row=2, column=2)

        self.loanAmount = StringVar()
        Entry(root, textvariable=self.loanAmount, justify=RIGHT).grid(row=3, column=2)

        self.monthlyPayment = StringVar()
        Entry(root, textvariable=self.monthlyPayment, justify=RIGHT).grid(row=4, column=2)

        self.totalPayment = StringVar()
        Entry(root, textvariable=self.totalPayment, justify=RIGHT).grid(row=5, column=2)

        btComputePayment = Button(root, text='compute Payment', command=self.computePayment)\
            .grid(row=6, column=2, sticky=E)

        root.mainloop()

    def computePayment(self):
        monthlyPayment= self.getMonthlyPayment(
            float(self.loanAmount.get()),
            float(self.annualInterestRate.get()) / 1200,
            int(self.numberOfYear.get()))
        self.monthlyPayment.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPayment.get()) * 12 * int(self.numberOfYear.get())
        self.totalPayment.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
                         (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

LoanCalculator()

