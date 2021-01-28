#Greenwhich Mean Time (GMT)
#Pakistan Time : GMT + 5
import time

currentTime = time.time() #gives the time in seconds covert into H:M:S
print(currentTime)
totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60

#Obtian the current minutes
totalMinutes = totalSeconds // 60

#compute the current minute in the hour
currentMinutes = totalMinutes % 60

#total hours
totalhour = totalMinutes // 60

#compute the current hours
currentHour = totalhour % 24
pakistanTime = currentHour + 5

if pakistanTime > 12:
    pakistanTime = pakistanTime % 12
print("Current time is: ",  pakistanTime,":",currentMinutes,":",currentSeconds)