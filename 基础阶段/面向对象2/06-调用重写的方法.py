class Animal:
    def eat(self):
        print('...吃...')
    def drink(self):
        print('...喝...')
    def sleep(self):
        print('...睡...')
    def run(self):
        print('...跑...')


class Dog(Animal):
    def bark(self):
        print('...汪汪叫...')

class Cat(Dog):
    def bark(self):
        print("狂叫")

        #方法1
        #Dog.bark(self)#self必须要写

        #方法2
        super().bark()


wangcai = Dog()
wangcai.eat()

tom = Cat()
tom.bark()
