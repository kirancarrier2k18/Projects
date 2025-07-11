#constructor is used to assgin the memory to the objected created
#destructor is used to clean up that assigned memory of the object

class Try:
    def __init__(self):
        print("The Constructor called object created")
    def __del__(self):
        print("Destructor")


ob1=Try()
ob2=Try()

#here the Destructor is printing automaticaly because the script is deleting the objects to save memroy

del ob1 # which will del or clean up the mem of the object
