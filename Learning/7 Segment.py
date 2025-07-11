
a = {"0": 6, "6": 6, "9": 6, "1": 2, "2": 5, "3": 5, "5": 5, "4": 4, "7": 3, "8": 7}

one = 0

x = (input("Enter the number: "))
for i in x:
    one += a[i]

print(one)