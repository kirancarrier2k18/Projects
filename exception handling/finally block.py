import sys

try:

    x=open("text_file.txt","r")
    y=x.read()
    print(y)
except:
    print("There is some exception as show below")
    print(sys.exc_info())
finally:
    x.close()
    print("Finally block executed")