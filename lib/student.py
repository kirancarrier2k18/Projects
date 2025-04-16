class Student:
    def __init__(self,Name,Age,Roll_Number,Marks):
        self.Name=Name
        self.Age=Age
        self.Roll_Number=Roll_Number
        self.Marks=Marks
    def Status(self):
        print(f"{self.Name} is present today")

    def Results(self):
        if self.Marks>=35:

            print(f"{self.Name} is Passed")

        else:
            print(f"{self.Name} is Failed")

#Student1=Student("Sai Kiran",26,12345,99)
#Student1.Status()
#Student1.Results()