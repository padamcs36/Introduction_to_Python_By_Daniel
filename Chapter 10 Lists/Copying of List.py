# list = [1,2,3]
# list1 = [3,4,5,6]
# print(id(list)) #both list having different memory location
# print(id(list1))
#
# list1 = list #Now assigning the list to list1, now id number is same for both because
#              #list1 is reference of list.
# print(id(list1))
#
# #If you want to copy one list of data to another list then apply this method
# list1 = [x for x in list]
# print(id(list1))
# list1 = [] + list
# print(id(list1))


list1 = list(range(1, 10,2))
print(list1)
