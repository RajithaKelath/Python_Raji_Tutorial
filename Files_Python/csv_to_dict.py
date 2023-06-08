import csv

list_to_dict = []

#read file
def convert_list_to_dict():

    with open('c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/csv_data.txt', mode='r' ) as file:
        next(file) # It throws away the first line of the data file
        file_text = [line.strip('\n').split(',') for line in file]
        for row in file_text:
            dct_store = {f"Name:{row[0]}, Category: {row[1]}, Main category: {row[2]}"}
            list_to_dict.append(dct_store)


def write_dict_to_file():
    file =  open('c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/json_data.txt','w')
    for line in list_to_dict:
        file.write(str(line) + ',' + '\n')

convert_list_to_dict()
write_dict_to_file()