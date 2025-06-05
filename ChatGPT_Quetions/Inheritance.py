# Create a base class Animal with a method make_sound(). Inherit it in two subclasses Dog and Cat, each overriding the make_sound() method.

class Animal:

    def make_sound(self):
        print("This is the sound of Animal")

class Dog(Animal):

    def make_sound(self):
        print("Bow Bow")

class Cat(Animal):

    def make_sound(self):
        print("Meow Meow")



pitbull=Dog()
pitbull.make_sound()
cat1=Cat()
cat1.make_sound()


