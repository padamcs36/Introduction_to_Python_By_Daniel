def main():
    millis = eval(input("Enter no: of milliseconds: "))
    convertMillis(millis)

def convertMillis(millis):
    seconds = millis / 1000
    currentSeconds = int(seconds) % 60

    # Obtian the current minutes
    totalMinutes = int(seconds) // 60

    # compute the current minute in the hour
    currentMinutes = totalMinutes % 60

    # total hours
    totalhour = totalMinutes // 60

    # compute the current hours
    # currentHour = totalhour % 24
    # pakistanTime = currentHour + 5
    print(totalhour,":",currentMinutes,":",currentSeconds)

main()