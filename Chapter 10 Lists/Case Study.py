#Todo Reverse the list
# def main():
#     lst = [1,2,3,4,5]
#     print(reverse(lst))
#     for value in lst:
#         print(value, end=' ')
#
# def reverse(lst):
#     newLst = len(lst) * [0]
#     print(newLst)
#     for i in range(len(lst)):
#         newLst[i] = lst[len(lst) - 1 - i]
#     lst = newLst
#     return lst
# main()

# TODO remove repeated numbers from the list
# def main():
#     list1 = m(1)
#     print(list1)
#
#     list2 = m(1)
#     print(list2)
#
# def m(x, lst = [1,1,2,3]):
#     # for i in range(len(lst)):
#     if x in lst:
#         lst.remove(x)
#     return lst
# main()

def main():
    list1 = m(1, [1,1,3,4,5])
    print(list1)
    list2 = m(1)
    print(list2)
def m(x, lst = None):
    if lst == None:
        lst = [1, 1, 2, 3]
    if x in lst:
        lst.remove(x)
    return lst
main()