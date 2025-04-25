class parent:

    def __init__(self):
        self.x=10
        self.y=20
        self.z=30

    def show(self):
        print(self.x,"Pulled from parent")
    def details(self,x):
        print(self.x,"pulled from the parent ")



class child(parent):
    def __init__(self):
        self.a=70
        self.b=80
        self.c=90
    def show(self):
        print(self.a,"Pulled from child")

    def details(self, a,b):
        print(self.a,self.b, "pulled from the parent ")

ob1=parent()
ob2=child()

ob1.show()
#ob2.details()
ob1.details(10)
ob2.details(20,30)


