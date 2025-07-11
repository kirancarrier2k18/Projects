class Thing:

    def __init__(self,Name,Weight,type):
        self.Name=Name
        self.Weight=Weight
        self.type=type

    def Greeting(self):
        print(f"Hi {self.Name}, Your Weight is {self.Weight} and you are a {self.type}")

    def Details(self):
        print("self.Name")
        print("self.Weight")
        print("self.type")


Mobile=Thing("Iphone 11","180 Grams","Mobile")
Vehicle=Thing("Car","500 KG","Mobile")
Mobile.Greeting()
Mobile.Details()

Vehicle.Greeting()
Vehicle.Details()