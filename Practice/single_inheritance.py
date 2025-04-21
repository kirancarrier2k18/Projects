
#Single inheritance

class Parent:
    def __init__(self):
        print("This is the Parent constructor")
    def parent_method(self):
        print("This is the Parent Method")

class Child(Parent):  #we have added the Parent here from which the child is going to be inherent
    def __init__(self):
        print("This is the child constructor")
    def child_method(self):
        print("This is the Child Method")

Parent_object=Parent()
Child_object=Child()

Parent_object.parent_method() # this is normal and this should print the Parent method line
Child_object.child_method() # even this is normal and this should print the child method line

#But when we call the parent method from the child object. even that works as we have added the parent in the child as child(Parent)

Child_object.parent_method()
#Parent_object.child_method() # this doesn't work and throws an error.

