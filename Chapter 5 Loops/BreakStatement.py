#break statement break out of the loop
#contionue statement break out the iteration
sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break #continue
print("Sum is ", sum)
print("number is ", number)