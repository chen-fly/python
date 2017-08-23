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
    def eat(self):
        print("自己吃")

wangcai = Dog()
wangcai.eat()

tom = Cat()
tom.eat()
