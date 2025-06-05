import sys

try: #our code
    y=10
    x=int(input("Enter the number: "))
    z=y/x
    print(Z)
except: # this will get executed if any exception occured
    print("There is an exception occured")
    print(sys.exc_info())

else: # this will get executed if there is no execption
    print("There is no exception")
finally: # this will get executed anyhow no matter exeception ocured or not.
    print("executed finally")


# we can also print the exception by sys.exc_info which is there in the sys module
