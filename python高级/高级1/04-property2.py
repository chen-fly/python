class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        print('get')
        return self.__num

    @num.setter
    def num(self, newNum):
        print('set')
        self.__num = newNum

    num = num = property(getNum, setNum)


t = Test()

t.num(200)  #相当于调用了 t.setNum(200)

print(t.num) #相当于调用了 t.getNum()
