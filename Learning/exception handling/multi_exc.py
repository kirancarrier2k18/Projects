
import sys
from math import expm1

try:
    var1=10
    var2=2
    if var2==0:
        raise ZeroDivisionError # raising the exception forvefully
    list1=[1,2,3]
    list1[2]=var1/var2
    print(list1[3])
except ZeroDivisionError:
    print("Numbers can't be divided by zero")
except ValueError:
    print("It is a value error")
except IndexError:
    print("The index is out of range")
except:
    print("some exception occured  ")
    print(sys.exc_info())

