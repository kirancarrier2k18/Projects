


class human:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def human_Details(self):
        print(f"the name of the person is {self.name} and he/she is {self.age} years old")

class employee(human):

    def __init__(self,name,age,Badge_ID):
        #self.name = name
        #self.age = age
        super().__init__(name,age) # this has to call the constructor of the parent class i.e human
        self.Badge_ID=Badge_ID

    def employee_Details(self):
        print(f"the name of the person is {self.name}, {self.age} years old and the Emp ID is {self.Badge_ID}")


object_one=human("Sai Kiran",26)
object_one.human_Details()

object_two=employee("Sai Kiran",26,1234)Haa

object_two=employee("Sai Kiran",26,120120)
object_two.employee_Details()


