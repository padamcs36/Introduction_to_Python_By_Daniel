import time

def main():
    beginTime = time.time()

    for p in range(2, 31 + 1):
        i = 2 ** p - 1 #it is also a prime number.

        # Display each number in five positions
        if isPrime(i):
            print(p, "\t", i)

    endTime = time.time()
    print("Time spent is", endTime - beginTime, "milliseconds")

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1

    return True  # number is prime
main()