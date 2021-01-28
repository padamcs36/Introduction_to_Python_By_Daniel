import random
NO_OF_TRIALS = 1000000
numberofHits = 0

for i in range(NO_OF_TRIALS):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x*x + y*y <= 1:
        numberofHits += 1
print(numberofHits)
pi  = 4 * numberofHits / NO_OF_TRIALS
print("PI is ", pi)