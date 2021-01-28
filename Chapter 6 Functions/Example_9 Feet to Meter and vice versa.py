'''
print(format(celsius, "<15d"), format(celsiusToFahrenheit(celsius), "<15.2f"), "  |    ",
    format(farenheit, "<15d"), format(fahrenheitToCelsius(farenheit), "<15.2f"))
'''

def main():
    print(format("Feet", "<15s"), format("Meter", "<15s"),"   |  ",
          format("Meter", "<15s"), format("Feet", "<15s"))
    print("--------------------------------------------------------------")
    i = 1
    metr = 20

    while i <= 10:
        print(format(i, "<15d"), format(footTometer(i), "<15.3f"), "   |   ",
              format(metr, "<15d"), format(meterToFoot(metr), "<15.3f"))

        metr += 6
        i += 1


def meterToFoot(meter):
    foot = meter / 0.305
    return foot
def footTometer(foot):
    meter = foot * 0.305
    return meter

main()