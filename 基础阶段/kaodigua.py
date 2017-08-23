class SweetPotato:
    
    def _init_(self):
        self.cookedstring = "生的"
        self.cookedLevel = 0
    def cook(self, cooked_time):
        if cooked_time >=0 and cooked_time < 3:
            self.cookedstring = '生的'
        
# 创建了一个地瓜对象        
di_gua = SweetPotato()

di_gua.cook()