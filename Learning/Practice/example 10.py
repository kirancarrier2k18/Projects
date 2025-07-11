

class Employee:

    def __init__(self):
        self.Name="Sai Kiran"
        self._ID=100
        self.__Package=120000


    def Public_method(self):
        print("This is the public method")
        print(self.__Package)

    def _Protected_method(self):
        print("This is the Protected Method")

    def __Private_method(self):
        print("this is the private method")


EMP1=Employee()
print(EMP1.Name)
print(EMP1._ID)
#print(EMP1.__Package) # This throws an error as the variable is private and this can't be accessed outside the class without method
EMP1.Public_method()
EMP1._Protected_method()
#EMP1.__Privated_method # even this method is private hence can't be able to access
EMP1._Employee__Private_method() # this is a hack to access the private method which is not legal.




