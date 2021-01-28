from Loan import Loan
def main():
    # Enter yearly interest rate 5
    annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: "))
    numberOfYear = eval(input("Enter number of year in an integer: "))
    loanAmount = eval(input("Enter number of loan amount e.g 12000: "))
    borrower = input("Enter borrower's name: ")

    # Create a Loan objec
    loan = Loan(annualInterestRate, numberOfYear, loanAmount, borrower)
    loan.setBorrower('Padam')

    # Display loan date, monthly payment, and total payment
    print("\nLoan is for ", loan.getBorrower())
    print("The monthly payment is ", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is ", format(loan.getTotalPayment(), ".2f"))
main()