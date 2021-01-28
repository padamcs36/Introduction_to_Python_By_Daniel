#check wether the number is prime or not
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            #condition is true it means number is not prime
            return False
        divisor += 1
    return True #Number is prime.

def printPrimeNumber(numberOfPrimes):
    # NUMBER_OF_PRIMES = 50
    NUMBER_OF_PRIMES_PER_LINE = 10
    count = 0
    number = 2

    while count < numberOfPrimes:
        if isPrime(number):
            count += 1

            print(format(number, "<5d"), end=" ") #print prime number
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
                print()
        #check next number is prime or not
        number += 1
def main():
    # print("The first 50 prime number are ")
    prime = eval(input("How many prime number you want to print."))
    printPrimeNumber(prime)
main()
