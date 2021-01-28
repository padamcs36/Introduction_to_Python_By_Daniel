NUMBER_OF_PRIMES = 2000 #number of primes to display
NUMBER_OF_PRIMES_PER_LINES = 8
count = 0
number = 2 #A number to be tested for the primeness

print("Print first 2000 Prime Number")
while count < NUMBER_OF_PRIMES:
    isPrime = True

    #Test if the number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0: #it is true means number is not prime
            isPrime = False
            break # exit the group and number is incremented by 1 (Line 27)
        divisor += 1

    #diplay the prime number and increase the count
    if isPrime:
        count += 1

        print(format(number, "8d"), end='')
        if count % NUMBER_OF_PRIMES_PER_LINES == 0:
            print() #Jump to new line when count = 10

    #check if the next number is prime
    number += 1