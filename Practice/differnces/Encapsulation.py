class Car:
    def __init__(self, brand, color, mileage):
        self.__brand = brand  # Private attribute
        self.__color = color  # Private attribute
        self.__mileage = mileage  # Private attribute

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        self.__mileage = mileage

# Example usage
my_car = Car("Toyota", "Red", 15000)
print(my_car.get_brand())  # Output: Toyota
my_car.set_color("Blue")
print(my_car.get_color())  # Output: Blue
