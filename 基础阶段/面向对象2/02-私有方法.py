class Dog:
    #私有方法  前面加两个下划线
    def __send_msg(self):
        print("......正在发送短信......")

    #共有方法
    def send_msg(self, new_money):
        if new_money>10000:
            self.__send_msg()
        else:
            print("......余额不足......")


dog = Dog()
dog.send_msg(1000000)
