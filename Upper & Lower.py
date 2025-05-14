name = "Sai KiraN"
Upper = 0
Lower = 0

for x in name:
    if x.isupper():
        Upper += 1
    elif x.islower():
        Lower += 1
print(Upper)
print(Lower)
