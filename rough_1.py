from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self,r):
        print(f"the area of the given circle is {3.14*r*r}")

class Rectangle(Shape):
    def area(self,a,b):
        print(f"The area of the given rectangle is {a*b}")

ob1=Circle()
ob1.area(4)
ab2=Rectangle()
ab2.area(4,2)


