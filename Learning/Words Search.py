def Words(lst):
    a=[]
    for i in lst:
        if i[0]== "s" or  i[0]=="S":
            a.append(i)
    return a



x=Words(["Sai","Hello","sri devi","Dell","AMD","super"])
print(x)



