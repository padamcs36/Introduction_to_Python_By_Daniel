#Fess increase every year 5% = 0.05
year = 1
TUITION_FEES = 10000
TotalFess = 10000
FourYear = 10000
while year <= 10:
    TotalFess += TUITION_FEES * 0.05
    if year <= 4:
        FourYear += TUITION_FEES * 0.05
    year += 1
print(TotalFess, FourYear)

