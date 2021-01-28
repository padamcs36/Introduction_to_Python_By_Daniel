i = 1
sum =0
count = 0
while i < 4:
    count += 1
    if i % 3 == 0:
        # continue
        break
    sum += i
    i += 1
print(sum)
sum1 = 0
for i in range(9):
    if i % 3 == 0:
        continue
    sum1 += i
print(sum1)