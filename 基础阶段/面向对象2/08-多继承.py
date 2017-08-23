# 默认继承 object 类
class Base:
    def test(self):
        print("===base===")

class A(Base):
    def test1(self):
        print('...test1')

class B(Base):
    def test2(self):
        print('...test2')

class C(A, B):
    pass

c = C()
c.test2()
c.test1()
c.test()
