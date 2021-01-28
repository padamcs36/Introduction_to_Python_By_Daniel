class MaxNumber:
    def findMax(self):
        number = int(input("Enter any integer number: "))
        max2 = number
        while number != 0:
            number = int(input("Enter any integer number: "))
            if number > max2:
                max2 = number
        print("Max number ::", max2)
        print("Number is : ",  number)
obj = MaxNumber()
obj.findMax()