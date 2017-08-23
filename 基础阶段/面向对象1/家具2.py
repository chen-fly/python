class Home:
    def __init__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        msg = "房子的面积是:%d,可用面积是:%d,户型是:%s,地址是:%s"%(self.area, self.left_area, self.info, self.addr)
        msg += "家具有:%s"%(self.contain_items)
        return msg

    def add_item(self, item):
        self.left_area -= item.area
        self.contain_items.append(item.name)

class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        msg = "%s的占地面积是:%d"%(self.name, self.area)
        return msg

fangzi = Home(129, "三室一厅", "北京市 朝阳区")
print(fangzi)

bed1 = Bed("席梦思", 4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)

bed2 = Bed('单人床', 2)
fangzi.add_item(bed2)
print(fangzi)
