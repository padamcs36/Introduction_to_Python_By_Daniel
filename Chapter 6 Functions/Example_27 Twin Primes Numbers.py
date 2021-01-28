def main():
    i = 2
    count = 1
    while count <= 100:
        if isPrime(i):
            temp = i
            print(i, end="  ")
            if count % 10 == 0:
                print()
            count += 1
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True
main()