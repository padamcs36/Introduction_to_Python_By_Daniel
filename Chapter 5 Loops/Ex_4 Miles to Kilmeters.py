#Program to covert the miles into the kilometers
#1Mile = 1.609 km
KM = 1.609
print("Miles        Kilometers")
for i in range(1, 11):
    print(i, end='')
    print(format(i * KM, "17.3f"))