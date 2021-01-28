#Program to convert the decimal number into the Hexadecimal
decimal = eval(input("Enter decimal value (0 to 15): "))
if decimal <= 9:
    print("The hex value is ",decimal)
elif decimal >= 10 and decimal <= 15:
    print("The hex value is ", chr(55 + decimal))
else:
    print("Invalid Input")

#Program to convert Hexadecimal to Decimal number.
Alpha = ['A', 'B', 'C', 'D', 'E', 'F']
Hexdecimal = input("Enter Hexadecimal value (0 t0 9 and A to F): ")
if Hexdecimal <= str(9):
    print("The decimal value is ",Hexdecimal)
elif Hexdecimal >= 'A' or Hexdecimal <= 'F':
    print("The hex value is ", 75 - ord(Hexdecimal))
else:
    print("Invalid Input")