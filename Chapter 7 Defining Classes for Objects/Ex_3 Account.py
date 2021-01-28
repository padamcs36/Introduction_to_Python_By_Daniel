class Account:
    def __init__(self, id = 0, blance = 100.0, annualInterestRate = 0):
        self.__id = id
        self.__blance = blance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id

    def getBlance(self):
        return self.__blance
    def setBlance(self, balance):
        self.__blance = balance

    def getAnnualInterstRate(self):
        return self.__annualInterestRate
    def setAnnualInterestRate(self, annualInterstRate):
        self.__annualInterestRate = annualInterstRate

    def getMonthlyInterestRate(self):
        monthlyInterestRate = self.__annualInterestRate / 12 / 100
        return self.__blance * monthlyInterestRate

    def withdraw(self, amount):
        if amount < self.__blance:
            self.__blance = self.__blance - amount
            return "You withdraw "+str(amount)
        else:
            return "unsufficient Balance"
    def deposit(self, amount):
        self.__blance = amount + self.__blance

def main():
    acountdetails = Account(1122, 20000, 4.5)

    print("Your Id ", acountdetails.getId())
    print("Your current balance ", acountdetails.getBlance())
    print("Your monthly InterestRate is ", acountdetails.getMonthlyInterestRate())
    print(acountdetails.withdraw(2500.50))
    print("You current Bank balance is: ",acountdetails.getBlance())
    acountdetails.deposit(5000)
    print("You balance: ", acountdetails.getBlance())

main()