class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(self.__maxprice)

    def set_maxprice(self,price):
        self.__maxprice = price
        print(self.__maxprice)

obj = Computer()
obj.set_maxprice(1000)