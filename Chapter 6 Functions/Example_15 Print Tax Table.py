import sys
#Prompt the user to enter the status

def main():
    print(format("Taxable Income","<20s"),format("Single","<10s"),format("Married Joint","<20s"),
          format("Married Separate","<20s"),format("Head of a House","<20s"))
    i = 50000
    while i <= 60000:
        print(format(i,"<20d"),format(computeTax(0, i),"<10.0f"),format(computeTax(1,i),"<20.0f"),
              format(computeTax(2,i),"<20.0f"),format(computeTax(3,i),"<15.0f"))
        i += 50

# status = eval(input("(0-single filer, 1-married Jointly, \n"+
#                     "2-married separately, 3-head of household)\n +"
#                     "Enter the filling status: "))
# income = eval(input("Enter taxable income: "))

#compute tax
tax = 0
def computeTax(status, income):
    global tax
    if status == 0: #compute tax for the single filer
        if income <= 8350:
            tax = income * 0.10
            return tax
        elif income <= 33950:
            tax = (8350 * 0.10) + (income - 8350) * 0.15
            return tax
        elif income <= 60000:
            tax = (8350 * 0.10) + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
            return tax

    elif status == 1:
        if income <= 16700:
            tax = 16700 * 0.10
            return tax
        elif income <= 60000:
            tax = (16700 * 0.10) + (income - 16700) * 0.15
            return tax

    elif status == 2:
        if income <= 8350:
            tax = income * 0.10
            return tax
        elif income <= 33950:
            tax = (8350 * 0.10) + (income - 8350) * 0.15
            return tax
        elif income <= 60000:
            tax = (8350 * 0.10) + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
            return tax

    elif status == 3:
        if income <= 11950:
            tax = 11950 * 0.10
            return tax
        elif income <= 45500:
            tax = (11950 * 0.10) + (income - 11950) * 0.15
            return tax
        elif income <= 60000:
            tax = (11950 * 0.10) + (45500 - 11950) * 0.15 + (income - 45500) * 0.25
            return tax

    else:
        print("Error: Invalid Status")
        sys.exit()

# #Display the result
# print("Tax is: ", format(tax, ".2f"))
main()