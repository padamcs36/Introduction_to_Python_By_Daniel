NUMBER_OF_PRIMES = 50 #number of primes to display
NUMBER_OF_PRIMES_PER_LINES = 10
count = 0
number = 2 #A number to be tested for the primeness

print("Print first 50 Prime Number")
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

        print(format(number, "5d"), end='')
        if count % NUMBER_OF_PRIMES_PER_LINES == 0:
            print() #Jump to new line when count = 10

    #check if the next number is prime
    number += 1

'''

# Python program to check if  
# given number is prime or not 
  
num = 11
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num//2): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 

'''