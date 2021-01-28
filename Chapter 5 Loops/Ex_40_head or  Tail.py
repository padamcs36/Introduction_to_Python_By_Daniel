import random
flip = 1
headSum = 0
tailSum = 0
while flip <= 1000000:
    toss = random.randint(0, 1)
    if toss == 1: #1 is for the head
        headSum += 1
    if toss == 0: #0 is for the tail
        tailSum += 1
    flip += 1

print("Heads Flips: ", headSum, "\t\tTails Flips: ", tailSum)