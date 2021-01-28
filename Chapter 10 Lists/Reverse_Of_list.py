def reverse(lst):
    result = []
    for x in lst:
        result.insert(0, x)
    return result

list = [1,2,3,4,5,6]
list1 = reverse(list)
print(list1)