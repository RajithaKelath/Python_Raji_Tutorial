#importing os module
import os

#get directory path
directory_path = os.getcwd()
print(directory_path)


#Open file in readable mode
my_file = open("c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/data.txt","r")

#read content from file to my_content
my_content = my_file.read()

#close file
my_file.close()

print(my_content)

#Open file in writable mode - it override content in file
my_file_write = open("c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/data.txt","w")

my_file_write.write('Bob')
my_file_write.close()

