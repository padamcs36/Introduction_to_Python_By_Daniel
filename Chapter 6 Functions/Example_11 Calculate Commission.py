'''
Sales Amount           Commission Rate
$0.01–$5,000           8 percent
$5,000.01–$10,000      10 percent
$10,000.01 and above   12 percent
'''

def main():
    print(format("Sales Amount", "<15s"), "   |   ", format("Commission", "<15s"))
    print("------------------------------")

    salesAmount = 5000

    while salesAmount <= 100000:
        print(format(salesAmount, "<23d"),
              format(computeCommission(salesAmount), "<15.2f"))
        salesAmount += 5000
commision = 0
def computeCommission(SalesAmount):
    if SalesAmount < 5000:
        commision = SalesAmount * 0.08
        return commision
    if SalesAmount >= 5000 and SalesAmount < 10000:
        commision = 5000 * 0.08 + (SalesAmount - 5000) * 0.1
        return commision
    if SalesAmount >= 10000:
        commision = 5000 * 0.08 + (10000 - 5000) * 0.1 + (SalesAmount - 10000) * 0.12
        return commision

main()