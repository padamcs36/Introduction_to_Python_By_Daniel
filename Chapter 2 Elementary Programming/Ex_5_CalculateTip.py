subtotal, gratuity = eval(input("Enter subtotal and gratuity rate: "))

gratuity = gratuity / 100 * subtotal
total = gratuity + subtotal
print(f"The gratuity is {gratuity} and the total is {total}")