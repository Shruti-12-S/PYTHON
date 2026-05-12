import json


'''Strings'''
# py_obj = {
#     "name":"shruti",
#     "isTeacher":True
# }

# json_str = json.dumps(py_obj)
# print(type(json_str), json_str)

# json_str = '{"name":"Shruti", "isTeacher": null}'

# py_obj = json.loads(json_str)

# print(type(json_str))
# print(type(py_obj), py_obj)


'''files'''
# with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/data.json","r") as f:
#     py_obj = json.load(f)
#     print(py_obj)

data = {
    "name":"shruti",
    "age":22,
    "isTeacher":True
}


with open("C:/Users/Shruti/OneDrive/Desktop/AIML PRIME 2.0/PYTHON/Python Fundamentals Part 5/data.json","w") as f:
    json.dump(data,f,indent=4, sort_keys=True)

