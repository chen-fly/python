class Dog(object):
    def __init__(self):
        print('-----init-----')
    def __del__(self):
        print('-----del-----')
    def __str__(self):
        print('-----str-----')
    def __new__(cls):
        print('-----new-----')
        obj =  object.__new__(cls)
        return obj


xtq = Dog()
