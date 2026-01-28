import json

# json_str= '{" name": "vijju" , "Is_student" : true}'
# py_obj = json.loads(json_str)

# print(type(py_obj))
# print(py_obj)

# #
# # dumps 
# #

# py_obj = {' name': 'vijju', 'Is_student': True}
# json_str= json.dumps(py_obj)

# print(json_str)
# print(type(json_str))


# # read 

# with open("mod 8/data.json", "r") as f:
#     py_obj= json.load(f)
#     print(py_obj)


# #
# # write
#

data={
    "name" : "vijju",
    "age" : 19,
    "address": " India"
    
}

with open("mod 8/data.json", "w") as f:
    py_obj= json.dump(data,f)
    print(py_obj)