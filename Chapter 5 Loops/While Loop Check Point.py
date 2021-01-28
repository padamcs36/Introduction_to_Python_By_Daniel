number = 100
while True:
    if number < 9:
        break
    number = number - 9
    print(number)
print("Number is ", number)

# number = 100
# while True:
#     if number < 9:
#         continue
#     number = number - 9
#     print(number)
# print("Number is ", number)
#Infinite Loop

print("Using Break Statement")
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            break
        print(i * j)
    print(i)

print("Using Continue Statement")
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            continue
        print(i * j)
    print(i)