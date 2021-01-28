'''
1dollar = 100 cents
1 quaters = 25 cents
1 dimes = 10 cents
1nikel = 5 cents
remaining are pennies
'''
totalCents = eval(input("enter amount, eg: 11.25 :=>"))
# totalCents = int(amount * 100)

dollar = totalCents // 100
remainingCents = totalCents % 100

quater = remainingCents // 25
afterQuaterCents = remainingCents % 25

dimes = afterQuaterCents // 10
afterDimesCents = afterQuaterCents % 10

nickel = afterDimesCents // 5
pennies = afterDimesCents % 5

print("Your amount", totalCents, "consists of\n",
      "\t", dollar, "dollars\n",
      "\t", quater, "quarters\n",
      "\t", dimes,  "dimes\n",
      "\t", nickel, "nickels\n",
      "\t", pennies, "pennies")