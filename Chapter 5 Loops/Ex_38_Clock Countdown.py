import time
# countDown = time.sleep(1)
No_Of_Seconds = eval(input("Enter the number of seconds: "))

while No_Of_Seconds >= 1:
    print(No_Of_Seconds, "seconds remaining")
    time.sleep(1)
    No_Of_Seconds -= 1
else:
    print("Stopped.")