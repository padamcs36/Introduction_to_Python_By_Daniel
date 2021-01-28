class Stock:
    def __init__(self, symbol, name, previousClosingPrice , currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getStockName(self):
        return self.__name

    def getStockSymbol(self):
        return self.__symbol

    def getStockPreviousPrice(self):
        return self.__previousClosingPrice

    def setStockPreviousPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getStockCurrentPrice(self):
        return self.__currentPrice

    def setStockCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangeParcent(self):
        percent = (self.__currentPrice - self.__previousClosingPrice) / \
                  (self.__previousClosingPrice) * 100
        return percent