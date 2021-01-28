count = 0
number = eval(input("Enter a number(0: for end of input):"))
max = number
while number != 0:
    if number > max:
        max = number
        count = 0
    if number == max:
        count += 1
    number = eval(input("Enter a number(0: for end of input):"))
print("The largest number is ", max)
print("The occurence count of the largest number is ",count)
