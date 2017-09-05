class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        print('set')
        self.__num = newNum

    def getNum(self):
        print('get')
        return self.__num

    num = num = property(getNum, setNum)


t = Test()

#print(t.__num)

print(t.getNum())
t.setNum(200)
print(t.getNum())
print("-"*30)

t.num = 200 #相当于调用了 t.setNum(200)

print(t.num) #相当于调用了 t.getNum()
