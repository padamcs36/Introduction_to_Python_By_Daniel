factor = " "
number = eval(input("Enter Integer: "))
count = 2

while count <= number:
    while number % count == 0:
        if number % count == 0:
          factor = factor + str(count)+", "
          number = number // count
          count = count
    count += 1
print(factor)