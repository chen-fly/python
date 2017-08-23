# 默认继承 object 类
class Base:
    def test(self):
        print("===base===")

class A(Base):
    def test(self):
        print('...A')

class B(Base):
    def test(self):
        print('...B')

class C(A, B):
    pass
    #def test(self):
    #    print('...C')

c = C()
c.test()
