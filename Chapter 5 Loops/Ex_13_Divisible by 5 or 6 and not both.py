count = 0
number = 100

while number <= 200:
    if number % 5 == 0 or number % 6 == 0 and not(number % 5 == 0 and number % 6 == 0):
        print(str(number)+" ",  end='')
        count += 1
        if count == 10:
            print()
            count = 0
    number += 1