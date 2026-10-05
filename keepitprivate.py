class Myclass:
    __privatevar = 27

    def __privmeth(self):
        print('I am inside Myclass')

    def hello(self):
        print('__privatevar is :',Myclass.__privatevar)

obj = Myclass()
obj.hello()
obj.__privmeth()