#Using Zeller's congruence algorithm to calculate the the day of the week by using:
# h = (q + | 26(m + 1)/10| + k + |k/4| + |j/4| + 5 + j) % 7
# where h is the day of the week : 0: saturday, 1:sunday, and 6: Friday
# q is day of the month
# m is the month (3= march, 4=April, 12-december, 13-Jan, Feb-14)
# j is the century |year/ 100|
# k is the year of the century ( year % 100).

days = {0:"Saturday", 1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday"}

year = eval(input("Enter year (e.g 2008): "))
m = eval(input("Enter month 1-12: "))
q = eval(input("Enter day of the of the month 1-31: "))

# if m == 1:
#     m = 13
#     year = year - 1
# if m == 2:
#     m = 14
#     year =  year - 1
if m >= 3:
    m = m + 2
j = (year / 100) // 1
k = (year % 100)

h = (q + (((26 * (m + 1)) / 10) // 1) + k + ((k / 4) // 1) + ((j / 4) // 1) + 5 + j) % 7

print(f"Day of the week is {days[h]}")