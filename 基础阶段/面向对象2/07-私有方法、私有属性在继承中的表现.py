class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print('...test1...')

    def __test2(self):
        print('...test2...')

    def test3(self):
        print(self.__num2)
        self.__test2()


class B(A):
    pass

b = B()
b.test1()
# 私有方法不会被继承
#b.test2()

print(b.num1)
# 私有属性不会被继承
#print(b.__num2)

b.test3()
