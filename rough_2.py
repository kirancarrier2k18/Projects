class BankAccount:

    def __init__(self,name,AC,bal):
        self.name=name
        self.__AC=AC
        self.__bal=bal
        #print(self.name,self.__AC)

    def Detials(self):
        print(self.name,self.__AC,self.__bal)

ob1=BankAccount("Sai Kiran","12349",1000000000)
#print(ob1.AC) # this should throw an error as AC is private variable
print(ob1.name) # this should work as the name is public variable
ob1.Detials()



