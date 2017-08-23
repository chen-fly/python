class Dog(object):
    __flag = None

    def __new__(cls):
        if cls.__flag == None:
            cls.__flag = object.__new__(cls)
            return cls.__flag
        else:
            return cls.__flag


a = Dog()
print(id(a))
b = Dog()
print(id(b))
