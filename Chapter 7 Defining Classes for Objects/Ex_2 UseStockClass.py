from Ex_2_Stock import Stock

def main():
    stock = Stock('Intel Corporation', 'INTC', 20.5, 20.35)
    print("The Stock Name ",stock.getStockName())
    print("The Stock Symbol ", stock.getStockSymbol())
    print("The Price Percent Change", format(stock.getChangeParcent(),".2f"),"%")

main()