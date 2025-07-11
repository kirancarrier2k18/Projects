from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    @abstractmethod
    def display_info(self):
        pass

class Sedan(Car):
    def display_info(self):
        print(f"Sedan - Brand: {self.brand}, Color: {self.color}, Mileage: {self.mileage}")

class SUV(Car):
    def display_info(self):
        print(f"SUV - Brand: {self.brand}, Color: {self.color}, Mileage: {self.mileage}")

# Example usage
my_sedan = Sedan("Honda", "White", 20000)
my_suv = SUV("Ford", "Blue", 30000)

my_sedan.display_info()  # Output: Sedan - Brand: Honda, Color: White, Mileage: 20000
my_suv.display_info()  # Output: SUV - Brand: Ford, Color: Blue, Mileage: 30000
