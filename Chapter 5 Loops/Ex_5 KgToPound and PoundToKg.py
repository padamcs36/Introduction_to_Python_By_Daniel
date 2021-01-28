#1kg = 2.2 Pound
KG = 2.2
count = 0
kilgrams = 20
pound =  1

print(format("kilograms", "<15s"), format("Pounds", "10s"),
      "      |     ", format("Pounds", "<15s"), format("Kilograms", "10s"))
print("--------------------------------------------------------------")
while count < 100:
    print(format(pound, "<15d"), format(pound * KG, "10.2f"), "      |      ", \
    format(kilgrams, "<15d"), format(kilgrams / KG, ".2f"))

    pound += 2
    kilgrams += 5
    count += 1
