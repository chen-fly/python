class Game(object):

    # 类属性
    num = 0

    # 实例方法
    def __init__(self):
        # 实例属性
        self.name = 'laowang'

    # 类方法
    @classmethod#装饰器
    def add_num(cls):
        cls.num += 1
        print(cls.num)

    # 静态方法
    @staticmethod
    def print_menu():
        print('1111')

game = Game()
Game.add_num()# 类方法可以通过类的名字调用
game.add_num()# 类方法可以通过实例对象的名字调用


Game.print_menu()# 通过类  调用静态方法
game.print_menu()# 通过实例对象  调用静态方法
