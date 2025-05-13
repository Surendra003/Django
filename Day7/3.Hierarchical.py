# Base class
class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        return f"{self.species} makes a sound."

# Derived class 1
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")  # Initialize the base class with species
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")  # Initialize the base class with species
        self.name = name
    def meow(self):
        return f"{self.name} says Meow!"
# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
# Calling methods from base class and derived classes
print(dog.speak())  # Output: Dog makes a sound.
print(dog.bark())   # Output: Buddy says Woof!
print(cat.speak())  # Output: Cat makes a sound.
print(cat.meow())   # Output: Whiskers says Meow!