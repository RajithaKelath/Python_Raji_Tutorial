import json

file = open('c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/json_data.txt','r')
file_content = json.load(file)

file.close()

print(file_content["json_data"][0])
"""
cars = [
    {"make" : "Ford" , "model" : "Fiesta"},
    {"make" : "Ford" , "model" : "Focus"}
]

file = open('c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/cars_json_write_file.txt','w')
json.dump(cars, file)

file.close()
"""