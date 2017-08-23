class Person(object):
    """创建人物"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None
        self.hp = 100

    def anzhuang_zidan(self, danjia_temp, zidan_temp):
        danjia_temp.yaru_zidan(zidan_temp)

    def anzhuang_danjia(self, gun_temp, danjia_temp):
        gun_temp.zhuangshang_danjia(danjia_temp)

    def naqiang(self, gun):
        self.gun = gun

    def __str__(self):
        if self.gun:
            return "%s的生命为:%d,手里拿着枪,%s"%(self.name, self.hp, self.gun)
        else:
            return "%s的生命为:%d,没有枪！"%(self.name, self.hp)

    def kou_ban_ji(self, target):
        print("%s向%s开了一枪"%(self.name, target.name))
        self.gun.fire(target)

    def diao_xue(self, zidan_temp):
        self.hp -= zidan_temp.sha_shang_li
        if self.hp > 0:
            return 0
        else:
            print("%s嗝儿屁了！！！"%self.name)

class Gun(object):
    """创建枪"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        self.danjia = None

    def zhuangshang_danjia(self, danjia):
        self.danjia = danjia

    def __str__(self):
        if self.danjia:
            return "枪的信息为:%s,%s"%(self.name, self.danjia)
        else:
            return "枪的信息为：%s,没有弹夹！"%self.name

    def fire(self,target):
        zidan_temp = self.danjia.zidan_list.pop()
        if zidan_temp:
            target.diao_xue(zidan_temp)
        else:
            print("弹夹空了！！！")


class Danjia(object):
    """docstring for Danjia."""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num
        self.zidan_list = []

    def yaru_zidan(self, zidan):
        self.zidan_list.append(zidan)

    def __str__(self):
        return "弹夹的信息为：%d/%d"%(len(self.zidan_list), self.max_num)

class Zidan(object):
    """docstring for Zidan."""
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li




def main():
    #1.创建一个人类
    xiaochen = Person("小陈")

    #2.创建一个枪类
    ak47 = Gun("AK47")

    #3.创建一个弹夹类
    danjia = Danjia(20)

    #4.创建一个子弹类
    zidan = Zidan(10)

    #5.子弹装入弹夹
    for i in range(15):
        xiaochen.anzhuang_zidan(danjia, zidan)

        #6.弹夹装在枪上
        xiaochen.anzhuang_danjia(ak47, danjia)

    #test:显示弹夹的信息
    #print(danjia)
    #test:显示枪的信息
    #print(ak47)

    #7.创建敌人
    diren1 = Person("毒枭")

    #8.拿枪
    xiaochen.naqiang(ak47)
    #test:查看人物的信息
    #print(diren1)
    #print(xiaochen)

    #9.开枪
    while diren1.hp >0:
        if diren1.hp:
            print(diren1)
        xiaochen.kou_ban_ji(diren1)



if __name__ == "__main__":
    main()
