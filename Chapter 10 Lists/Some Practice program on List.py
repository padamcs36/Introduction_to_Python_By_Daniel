#TODO Pass list Argument
# def main():
#     x = 1 #numbers are an immutable
#     y = [1,2,3] #lists are mutable
#     m(x, y)
#     print("X is ", x)
#     print("y[0] is ", y[0])
# def m(number, numbers):
#     number = 5
#     numbers[0] = 1010
#
# main()

#todo default list argument
def list(x, list=[]):
    if x not in list:
        list.append(x)
    return list
def main():
    list1 = list(1)
    print(list1)

    list2 = list(2)
    print(list2)

    list3 = list(5, [1,2,3,4])
    print(list3)

    #defualt list is still [1,2]
    list4 = list(4)
    print(list4)

main()