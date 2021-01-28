#write a program to predict the tuition in how many year fees is double
#every year fees is increase 7%
#Initial fees is $10000
year = 0
TUITION = 10000

while TUITION < 20000:
    year += 1
    TUITION = TUITION * 1.07
print(f"Tuition will be double in {year} years.")
print("Tuition will be $" + format(TUITION, ".2f"), "in", year, "years")