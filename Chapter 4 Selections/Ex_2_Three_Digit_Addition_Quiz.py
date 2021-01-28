#Generating random three number and guessing theirs output.
import random

rand1 = random.randint(0, 9)
rand2 = random.randint(0, 9)
rand3 = random.randint(0, 9)

guess = eval(input("What is "+str(rand1)+" + "+str(rand2)+" + "+str(rand3)+ "?"))
print(str(rand1)+" + "+str(rand2)+" + "+str(rand3)+" = "+str(rand1+rand2+rand3), rand1+rand2+rand3 == guess)