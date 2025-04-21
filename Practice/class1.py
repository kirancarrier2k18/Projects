
class greetings:

    "This is the Doc section of this Class"
    #Name=""
    def Method1(self,Name):
        print(f"Hello {Name}")


x=greetings()
x.Method1("Sai Kiran")
print(x.__doc__)

