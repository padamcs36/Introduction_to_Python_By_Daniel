months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sup", "Oct", "Nov", "Dec"]
Days = {months[0]:31,months[1]:28,months[2]:31,months[3]:30, months[4]:31, months[5]:30, months[6]:31, months[7]:31, months[8]:30, months[9]:31, months[10]:30, months[11]:31}
month, year = eval(input("Enter month and year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    Days["Feb"] = 29

print(months[month - 1], year ,"has", Days[months[month- 1]], "Days")