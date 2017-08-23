class Dog(object):
    def print_self(self):
        print("hello I'm 111")

class Xiaotq(Dog):
    def print_self(self):
        print("hello I'm 222")

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
