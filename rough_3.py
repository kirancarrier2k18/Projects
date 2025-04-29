class Animal:
    def __init__(self):
        print("This a animal contructor")

    def sound(self):
         print("Animal sound")

class Dog(Animal):

    def sound(self,Breed,colour):
        super().__init__()
        print(f"the Dog will say bow bow bow" )

class Cat(Animal):

    def sound(self):
        super().__init__()
        print("meow meow")

ob1=Dog()
ob1.sound("Sitzu","white")


