number = eval(input("Enter the number between 0 and 1000: "))

last = number % 10
remainingDigit = number // 10

middle  = remainingDigit % 10
first = remainingDigit // 10

print("The sum of the digits: ", last+middle+first)
