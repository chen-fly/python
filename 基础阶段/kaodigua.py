class SweetPotato:
    
    def _init_(self):
        self.cookedstring = "����"
        self.cookedLevel = 0
    def cook(self, cooked_time):
        if cooked_time >=0 and cooked_time < 3:
            self.cookedstring = '����'
        
# ������һ���ع϶���        
di_gua = SweetPotato()

di_gua.cook()