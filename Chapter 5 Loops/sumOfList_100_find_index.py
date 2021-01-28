'''Can someone help me to find what numbers add up to a certain sum from a list?
Like
If the sum is 100
And the list is 95, 4, 6, 1, 5
The answer is 0 and 4'''
list = [95, 4, 6, 1, 5]
sum1 = 100
result = 0
index = ''
count = 0
for i in range(len(list)):
    result += list[i]
    if result > sum1:
        result -= list[i]
        continue
    else:
        index = index + str(list.index(list[i]))
print(result, index)

nums = [95,4,6,1,5]
sum = 100
h = {}
for i, num in enumerate(nums):
    n = sum - num
    if n not in h:
        h[num] = i
    else:
        print([h[n], i])