class Car:


    def __init__(self,Brand,Colour,Number):
        self.Brand=Brand
        self.Colour=Colour
        self.Number=Number

    def Details(self):
        print(f"the Colour of the {self.Brand} car with {self.Number} is {self.Colour}")
    def Start(self):
        print(f"the {self.Brand} is started")

#car1=Car("Benz","Grey",12345)
#car1.Details()
#car1.Start()
