class sentinelValue:
    def __init__(self):
        self.sum = 0

    def add(self):
        data = int(input("Enter an integer (end the loop if input is 0): "))#sentinel value
        while data != 0:
            self.sum += data
            data = int(input("Enter an integer (end the loop if input is 0): "))

        print("Sum is: ", self.sum)
        # return self.sum

obj = sentinelValue()
obj.add()
