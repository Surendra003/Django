# Base class
class Animal:
    def __init__(self, species):
        self.species = species
    def eat(self):
        return f"{self.species} is eating."

# Derived class from Animal
class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species)  # Initialize the base class (Animal)
        self.fur_color = fur_color
    def breathe(self):
        return f"{self.species} breathes air."

# Further derived class from Mammal
class Dog(Mammal):
    def __init__(self, species, fur_color, name):
        super().__init__(species, fur_color)  # Initialize the base class (Mammal)
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"

# Create an instance of the Dog class
my_dog = Dog("Dog", "Brown", "Buddy")

# Call methods from all levels of the inheritance chain
print(my_dog.eat())        # Output: Dog is eating.
print(my_dog.breathe())    # Output: Dog breathes air.
print(my_dog.bark())       # Output: Buddy says Woof!