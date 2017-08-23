class Dog(object):
    __flag = None

    def __new__(cls, name):
        if cls.__flag == None:
            cls.__flag = object.__new__(cls)
            return cls.__flag
        else:
            return cls.__flag

    def __init__(self, name):
        self.name = name

a = Dog('旺财')
print(id(a))
print(a.name)

b = Dog('哮天犬')
print(id(b))
print(b.name)
