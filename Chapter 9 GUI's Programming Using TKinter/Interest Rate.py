from tkinter import *
class ComputeInterestRate:
    def __init__(self):

        tk = Tk()
        tk.title("Interest Rate")
        frame = Frame(tk)
        frame.pack()

        Label(frame, text='Loan Amount').pack(side=LEFT)
        self.amount = StringVar()
        Entry(frame, textvariable=self.amount).pack(side=LEFT)

        Label(frame, text='Years').pack(side=LEFT)
        self.year = StringVar()
        Entry(frame, textvariable=self.year).pack(side=LEFT)

        Button(frame, text='Calculate', command=self.calculate).pack(side=LEFT)

        fram1 = Frame(tk)
        fram1.pack()
        self.lbx = Listbox(fram1, width=70)
        self.lbx.pack()
        self.lbx.insert(END, format("Interest Rate            Monthly Payment         Total Payment"))
        # scrollbar = Scrollbar(fram1)
        # scrollbar.pack()
        #
        # self.text = Text(fram1, wrap=WORD, yscrollcommand=scrollbar.set)
        # self.text.pack()
        # # Scrollbar.config(command=self.text.yview)

        tk.mainloop()

    def calculate(self):
            InterestRate = 5
            while InterestRate <= 10:
                monthlyInterestRate = InterestRate // 1200
                monthlyPayment = float(self.amount.get()) * monthlyInterestRate / \
                                 (1 - 1 / (1 + monthlyInterestRate) ** (int(self.year.get()) * 12))

                # self.monthlyPayment.set(format(monthlyPayment, "10.2f"))
                totalPayment = float(monthlyPayment * 12 * int(self.year.get()))
                # self.totalPayment.set(format(totalPayment, "10.2f"))
                self.lbx.insert(ACTIVE, f'{InterestRate}, {monthlyPayment}, {totalPayment}')
                InterestRate += 1


ComputeInterestRate()
