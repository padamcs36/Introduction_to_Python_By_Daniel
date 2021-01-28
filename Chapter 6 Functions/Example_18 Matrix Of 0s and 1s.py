import random

def main():
    n = eval(input("Enter n: "))
    count = 0
    i = 1
    while i <= n*n:
        print(matrix() ,end='  ')
        count += 1
        if count % n == 0:
            print()
        i += 1
def matrix():
    OnesZeros = random.randint(0, 1)
    return OnesZeros
main()