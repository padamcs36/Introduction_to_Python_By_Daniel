'''
# Converts from Celsius to Fahrenheit def celsiusToFahrenheit(celsius):
# Converts from Fahrenheit to Celsius def fahrenheitToCelsius(fahrenheit):
The formulas for the conversion are:
celsius = (5 / 9) * (fahrenheit – 32) fahrenheit = (9 / 5) * celsius + 32
'''

def celsiusToFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return  fahrenheit

def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

print(format("Celsius", "10s"), "Fahrenheit",   "  | ", format("Fahrenheit", "12s"), "Celsius")
i=1
celsius = 40
fahrenheit = 120
while i <= 10:
    print(format(celsius, "<10d"), format(celsiusToFahrenheit(celsius), "<8.2f"), format("|", ">5s"),format(fahrenheit, "<12d"), format(fahrenheitToCelsius(fahrenheit), "<8.2f"))

    celsius -= 1
    fahrenheit -= 10
    i += 1

