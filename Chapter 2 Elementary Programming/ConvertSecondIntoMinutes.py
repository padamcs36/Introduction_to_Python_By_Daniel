#In this program user enters the number of seconds
#programs returns the number of minutes in remaining seconds

seconds = eval(input("Enter number of seconds: "))

minutes = seconds // 60 #Integer division gives the whole number = minutes
remainingSeconds = seconds % 60
print(seconds, " seconds is ",minutes, "minutes and", remainingSeconds, "seconds")

#Now converting the seconds into the Hours and minutes and seconds

second = eval(input("Enter number of seconds: "))
#computing the hours in the seconds
hour = second // 3600
remainingseconds = second % 3600
#computing the number of minutes that are left after the  hours
minute = remainingseconds // 60
leftSeconds = remainingseconds % 60

print(hour,":",minute,":",leftSeconds)