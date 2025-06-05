#Create a class Car with attributes make, model, and year. Initialize these using a constructor and display them using a method.

class Car:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def Display(self):

        print(f"{self.make}\n{self.model}\n{self.year}")

Car1=Car("Benz","E series","2024")
Car1.Display()


print(Car1.make)