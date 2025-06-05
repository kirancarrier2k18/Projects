# Create a class Person with attributes name and age. Add a method to display the person's details.

class Person:

    def Display(self,name,age):
        self.name = name
        self.age = age
        print(f"Hi {self.name}, Your age is {self.age}")


Student=Person()
Student.Display("Sharath","30")




