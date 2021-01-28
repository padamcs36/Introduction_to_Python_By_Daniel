import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

guess = eval(input(f"What is {str(num1)} + {str(num2)} ? "))
print(f"{num1} + {num2} = {num1 +  num2}", num1 + num2 == guess)