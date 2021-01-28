def decimalToHex(decimalValue):
    hex = " "
    while decimalValue != 0:

        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex #Calling the toHexChar method or individual checking the digit is greater than 9 or not
        decimalValue = decimalValue // 16 #is repeating utill  and unless it is zero.
    return hex

def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))
def main():
    decimalValue = eval(input("Enter a decimal value: "))
    print("The hex value for", decimalValue, "is", decimalToHex(decimalValue))
main() #call the main funcion