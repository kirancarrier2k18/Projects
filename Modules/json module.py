import json

x= {"Name":"Sai Kiran","Age":26}

print(x)
print(type(x))

json_format=json.dumps(x) # dumps will convert the dict format to json format that is "str format"
print(json_format)

print(type(json_format))


orginal_format= json.loads(json_format) # loads will convert the json str format to orginal format
print(orginal_format)
print(type(orginal_format))



