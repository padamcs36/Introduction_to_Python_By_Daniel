minutes  = eval(input("Enter the number of minutes: "))


Totaldays = minutes // 60 // 24

year = Totaldays // 365
days = Totaldays % 365

# year = minutes // 60 // 24 // 365
print(f"{minutes} minutes approximately {year} years and  {days} days")