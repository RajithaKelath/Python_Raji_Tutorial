import csv
import json

#create empty dictionary
dict_data = []
feilds = ["name","category","main_category"]
#read file
def convert_list_to_dict():

    with open('c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/csv_data.txt', mode='r' ) as file:
        #next(file) # It throws away the first line of the data file
        csv_reader = csv.reader(file) #as we are additionally adding feild, we can use csv.reader(file), if header included in csv raw data, then use csv.DictReader(file)

        for rows in csv_reader:
            dict_feild_data = dict(zip(feilds,rows))
            dict_data.append(dict_feild_data)

    file =  open('c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/json_data.txt','w')
    file.write('{' + '\n' + '\t' + '"json_data" :' + '\n'+ '\t' )
    json.dump(dict_data, file)
    file.write('\t'+ '\n' + '}' )

    file.close()

convert_list_to_dict()
#write_dict_to_file()


"""
#Alternate method 

import json
 
json_list = []      # store the converted json data for each line
csv_file = open('csv_file.txt', 'r')
 
for line in csv_file.readlines():
    club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)
 
csv_file.close()
 
json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)     # write json data to a file
json_file.close()
"""