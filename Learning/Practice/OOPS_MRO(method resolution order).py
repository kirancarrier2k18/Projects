class Base1:

    def __init__(self):
        print("this is the constructor of the base 1")
    def method(self):
        print("this is the Base one")

class Base2:
    def __init__(self):
        print("this is the constructor of base 2")
    def method(self ):
        print("this is the base two")

class Base3(Base1,Base2):
    def __init__(self):
        print("this is the constructor of base 3")


ob1=Base3()
ob1.method()