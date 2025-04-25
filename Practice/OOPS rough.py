class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"{self.name} is {self.age} old")

class employee(person):
    def __init__(self,name,age,employee_id):
        super().__init__(name, age)
        self.employee_id=employee_id

    def display_info(self):
        print(f"{self.name} is {self.age} old and the ID is {self.employee_id}")

ob1=employee("Sai Kiran",26,100)
ob1.display_info()

