from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, age):
        self.age = age

    @staticmethod
    def convert_pound_to_kg(w):
        return w*0.453592

    @abstractmethod
    def feed(self):
        pass

class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age)
        self.breed = breed

    def feed(self):
        print("The dog was fed")

    @classmethod
    def husky_puppy(cls):
        return cls(0, "husky")


print(Dog.convert_pound_to_kg(5))
d = Dog.husky_puppy()
print(d.breed, d.age, d)