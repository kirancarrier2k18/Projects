number=7
a=0
b=1
lst=[a,b]

for i in range(0,number-2):

    c=a+b
    a=b
    b=c
    lst.append(c)

print(lst)