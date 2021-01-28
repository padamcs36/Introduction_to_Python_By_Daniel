#Converting kilogram into the pound
#1kg = 2.2 pound
KG = 2.2

print("Kilograms     Pound")

for i in range(1, 200, 2):
    print(i, end='')
    print(format(i * KG, "17.2f"))