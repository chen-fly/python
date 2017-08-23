class Tool(object):

    # 类属性
    num = 0
    # 方法
    def __init__(self, new_name):
        # 实例属性
        age = 11
        self.name = new_name
        Tool.num += 1

# 实例属性实例单独享有，类属性，由多个实例对象所共有

tool1 = Tool("铁锹")
tool2 = Tool("兵工铲")
print(Tool.num)
