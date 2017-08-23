# coding = utf-8



class Zidan:
    def __init__(self, shashangli):
        self.shashangli = shashangli



class Danjia:
    
    def __init__(self, rongliang):
        self.danjiarongliang = rongliang
        self.zidanliebiao = []

    def zhuangzidan(self,zidan):
        self.zidanliebiao.append(zidan)
        print("zidan+1....num:%d"%len(self.zidanliebiao))
        
    def chuzidan(self):
        if len(self.zidanliebiao)>0:
            shashangli = self.zidanliebiao[-1].shashangli
            self.zidanliebiao.pop()
            print("zidan-1....num:%d"%len(self.zidanliebiao))
        else:
            shashangli = 0
        return shashangli





    

class Qiang:
    def __init__(self, name):
        self.name = name
        
    def huandanjia(self,danjia):
        self.danjia = danjia

    def fashe(self, mubiao):
        shashangli = self.danjia.chuzidan()
        mubiao.diaoxue(shashangli)
    
    
    
# 人    
class Ren:

    def __init__(self):
        self.shengmingzhi = 100

    def maiqiang(self, qiang):
        self.qiang = qiang
        print("yibaqiang")
        
    def yazidan(self, danjia, zidan):
        danjia.zhuangzidan(zidan)

    def zhuangdanjia(self, danjia):
        self.qiang.huandanjia(danjia)
        
    def kaiqiang(self, mubiao):
        self.qiang.fashe(mubiao)
        
    def diaoxue(self, shashangli):
        self.shengmingzhi -= shashangli
        print('shengyu:%d'%self.shengmingzhi)
        
        
        
        
        
        
xiaoming = Ren()

daju = Qiang('daju')

xiaoming.maiqiang(daju)


danjia = Danjia(100)


zidan = Zidan(5)

xiaoming.yazidan(danjia, zidan)

xiaoming.zhuangdanjia(danjia)

laowang = Ren()


xiaoming.kaiqiang(laowang)

















