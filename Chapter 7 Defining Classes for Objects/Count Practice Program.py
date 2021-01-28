# class Count:
#     def __init__(self, count = 0):
#         self.count = count
#
# def main():
#     c = Count()
#     times = 0 #integers are immutable cannot be changed outside the function
#     for i in range(100):
#         increment(c, times)
#
#     print("Count is ", c.count)
#     print("Time is", times)
# def increment(c, times):
#     c.count += 1
#     times += 1 #immutable integer so it cannot be changed/affect the outside times variable
#
# main()

class Count:
    def __init__(self, count = 0):
        self.count = count
def main():
    c = Count()
    n = 1
    m(c, n)
    print("count is", c.count)
    print("n is", n)
def m(c, n):
    c = Count(5)
    n = 3
main() # Call the main functio