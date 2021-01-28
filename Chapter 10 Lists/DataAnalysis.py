NUMBER_OF_ELEMENTS = 5
NUMBERS = []
sum = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = eval(input("Enter number of elements: "))
    NUMBERS.append(value)
    sum += value

average = sum / NUMBER_OF_ELEMENTS
count = 0
for i in range(NUMBER_OF_ELEMENTS):
    if NUMBERS[i] > average:
        count += 1
print("Average is ", average)
print("Number of elements above the average is ", count)