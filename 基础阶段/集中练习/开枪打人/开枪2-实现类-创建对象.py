class Person(object):
    """人的类"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name

class Gun(object):
    """枪类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name#用来记录枪的类型

class Danjia(object):
    """弹夹类"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num#用来记录弹夹的容量

class Zidan(object):
    """子弹类"""
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li#这颗子弹的威力




def main():
    """用来控制整个程序的流程"""

    #1.创建老王对象
    xiaochen = Person("小陈")

    #2.创建枪对象
    ak47 = Gun("AK47")

    #3.创建一个弹夹对象
    dan_jia = Danjia(20)

    #4.创建一些子弹
    zi_dan = Zidan(10)

    #5.把子弹安装到弹夹中
    #小陈。安装子弹到弹夹中（弹夹，子弹）
    xiaochen.anzhuang_zidan(dan_jia, zi_dan)

    #6.把弹夹安装到枪中

    #7.创建一个敌人

    #8.拿枪

    #9.开枪打人

if __name__ == '__main__':
    main()
