'''
Enter an integer:
Is 10 divisible by 5 and 6? False
Is 10 divisible by 5 or 6? True
Is 10 divisible by 5 or 6, but not both? True
'''
num = eval(input("Enter an number: "))

print(f"Is {num} divisible by 5 and 6? ", (num % 5 == 0 and num % 6 == 0) == True)
print(f"Is {num} divisible by 5 or 6? ", (num % 5 == 0 or num % 6 == 0) == True)
print(f"Is {num} divisible by 5 or 6, but not both? ", (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0))