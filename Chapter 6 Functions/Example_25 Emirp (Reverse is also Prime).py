def main():
    i = 2
    count = 1
    while count <= 100:
        if isPrime(i):
            if isPrime(reverse(i)) and i != reverse(i):
                print(i,  end="  ")
                if count % 10 == 0:
                    print()
                count += 1
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0: #number is not if condition is true.
            return False
        divisor += 1
    return True #True means number is prime

def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10
    return result
main()