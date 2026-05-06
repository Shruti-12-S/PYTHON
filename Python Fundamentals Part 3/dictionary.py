info = {
    "name":"Shruti",
    "cgpa":9.38,
    "subjects":["OOPs","DSA"],
    3.14:"PI"
}

info["cgpa"]=9.56

print(type(info))

print(info["name"])
print(info[3.14])
print(info)

'''Dictionary methods'''
dict_keys = list(info.keys())
print(dict_keys)
print(type(dict_keys))


dict_values = list(info.values())
print(dict_values)

print(info.items())

# print(info["cgpa2"])
print(info.get("name"))
print(info.get("cgpa2"))  # This will return None instead of raising an error


info.update({"city":"Delhi"})
print(info)