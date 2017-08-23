class Dog:
    def set_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

dog = Dog()
dog.set_age(12)
dog.age = 10
dog.name = "小白"

#dog.set_age(12)

print(dog.get_age())

#dog.get_age()
#dog.get_name()
