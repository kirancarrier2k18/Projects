class Car:
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Mileage: {self.mileage}")

class ElectricCar(Car):  # Inheriting from Car class
    def __init__(self, brand, color, mileage, battery_capacity):
        super().__init__(brand, color, mileage)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Mileage: {self.mileage}, Battery Capacity: {self.battery_capacity} kWh")

# Example usage
my_car = Car("Toyota", "Red", 15000)
my_electric_car = ElectricCar("Tesla", "Black", 10000, 75)

my_car.display_info()  # Output: Brand: Toyota, Color: Red, Mileage: 15000
my_electric_car.display_info()  # Output: Brand: Tesla, Color: Black, Mileage: 10000, Battery Capacity: 75 kWh
