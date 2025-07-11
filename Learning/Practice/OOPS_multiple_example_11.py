class Parent1:
    def __init__(self):
        print("This is the Parent1 constructor")
    def parent1_method(self):
        print("This is the Parent1 Method")

class Parent2:
    def __init__(self):
        print("This is the Parent2 constructor")
    def parent2_method(self):
        print("This is the Parent2 Method")

class child(Parent1,Parent2):
    def __init__(self):
        print("This is the Child constructor")
    def child_method(self):
        print("This is the Child Method")

ob1=child()
ob1.parent2_method()
ob1.parent1_method()
ob1.child_method()




