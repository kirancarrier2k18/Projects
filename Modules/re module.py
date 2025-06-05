import re # this is a patren matching module

# single search
'''


if re.search("python","python is a easiest coding language"):
    print("Python is there")
else:
    print("Python is not there")
    
'''
# to crete a filter --> re.findall("[abcd]at") <-- this can filter aat bat cat dat only..

# double search

x = "Python python python python"

allwords=re.findall("python",x)
print(len(allwords))
print(type(allwords))
for i in allwords:
    print(i)

# input=1234-123-1234
# for formatting
#re.search("[0-9]{4}-[0-9]{3}-[0-9]{4}")