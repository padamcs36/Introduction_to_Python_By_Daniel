# list = []
# print("Print 10 Numbers")
# for i in range(10):
#     list.append(eval(input()))
#
# print(list)

# s = input("Enter 10 number separated by spaces on one line")
# items = s.split() #Extract items from the strings
# list1 = [eval(x) for x in items] #convert items to numbers
# print(list1)

def shift(list):
    temp = list[0]

    #shift elements to left
    for i in range(1, len(list)):
        list[i - 1] = list[i]

    list[len(list) - 1] = temp
    return list
list = [2, 5, 6, 9, 3]
print(shift(list))