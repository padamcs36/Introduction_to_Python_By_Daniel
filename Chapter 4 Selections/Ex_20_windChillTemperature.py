#Calculatng the wind chill  temperature.
#formulla
#Twc = 35.74 + 0.621 * ta  - 35.75V^0.16 + 0.4275taV^0.16
#where ta is outside temp in F, v is the speed measured in miles per hour.
#Twc is wind chill temperature.
#formulla is valid if wind speed greater than or equal to 2mph
# temperature in between -58F and 41F

Ta = eval(input("Enter temp: in between -58F and 41: "))
v = eval(input("Enter wind speed greater than or equal to 2MPH: "))

if Ta >= -58 and Ta <= 41 and v >= 2:
    Twc = 35.74 + 0.621 * Ta - 35.75 * (v ** 0.16) + 0.4275 * Ta * (v ** 0.16)
    print("The wind chill index is: ", Twc)
else:
    print("The temperature and/or wind speed is invalid")
