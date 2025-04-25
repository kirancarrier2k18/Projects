class Grand_Parent:
    def method_1(self):
        print("This is the Grand Parent method")

class Parent(Grand_Parent):
    def method_2(self):
        print("This is the Parent method")

class Child(Parent):
    def method_3(self):
        print("This is the Child method")


ob1=Child()
ob1.method_3()
ob1.method_2()
ob1.method_1()