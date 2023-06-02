"""
print("Hello it\"s Me")

final_greeting = "Is this {name} and you are {age}"
raji_greeting = final_greeting.format(name='Raji',age=29)
print(raji_greeting)

your_name = input ("Enter your name: ")
print(f"Hello {your_name}, My name is Raji!")

#Ask user their age
user_age = int(input("Enter your age: "))
print(f"You lived for {user_age * 12}  months.")

#Any value that pass through bool() will be True/ Empty or zero will be False

default_name = "there"
user_name = input("Enter Your name (Optional): ")

name = user_name or default_name
print(f"Hello {name}!")

#sets
art_friends = {"Ram" , "Sita", "Vishnu"}
science_friends = {"Sita", "laxmi"}

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)
science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art)
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
art_and_scienct = art_friends.intersection(science_friends)
print(art_and_scienct)
all_friends = art_friends.union(science_friends)
print(all_friends)

#Dictionary
fruits = {"Apple": "Red" , "Mango": "Yellow", "Grapes": "Green"}
print("Color of Apple is " + fruits["Apple"])

"""
"""
fruits_color = (
  {"fruit":"Apple" , "Color": "Red"},
  {"fruit":"Mango" , "Color": {"Yellow","Green"}},
  {"fruit":"Grapes" , "Color": "Green"}
)
fruit = int(input("Which fruit color you want (0 for Apple,1 for Mango,2 for Grapes): "))

print(fruits_color[fruit]["fruit"] + " colour is " + str(fruits_color[fruit]["Color"]))
print(len(fruits_color[fruit]["Color"]))
"""
"""
lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {"name": "Bob", "numbers": {1,5,22}},
    {"name": "Ann", "numbers": {5,7,9}}
    ]

player1_num = players[0]["numbers"]
print(player1_num)

player1_name = players[0]["name"]
match = player1_num.intersection(lottery_numbers)

print("Player " + player1_name + " got " + str(len(match)) + " numbers right." )


#Joins test
friend = ["Ram", "Sita", "Vishnu"]
comma_separator = ", ".join(friend)
print(f"My friends are {comma_separator}.")

#if else statement
friends = ["Jenny", "Charlie", "Bob"]
family = ["Ram", "Sita"]

user_name = input("Enter your name: ")

if user_name in friends:
  print("Hello Friend!")
elif user_name in family:
  print("Hello Family!")
else:
  print("Hello stranger")

user_input = input("Would you like to run program (p/q): ")

while user_input != "q":
    if user_input == "p":
        print("Hello")
    user_input = input("Would you like to run program (p/q): ")

for i in range(1, 101):
    if (i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

"""
"""
#Pattern Printing

num_line = int(input("Enter number of lines: "))

pattern = [print("* " * num) for num in range(1, num_line+1)]

"""
"""
#Reverse Pattern Printing

#num_line = int(input("Enter number of lines: "))

num_line = int(input("Enter number of lines: "))

pattern = [print("* " * num) for num in reversed(range(1, num_line+1))]
"""
"""
#Diamond printing

num_line = int(input("Enter number: "))
space = num_line // 2
star = 1

while star <= num_line:
  print((" " * space) + ("*" * star)) 
  space = space - 1
  star = star + 2

space = space + 1
star = star - 2
  
while star > 0:
  space = space + 1
  star = star - 2
  print((" " * space) + ("*" * star)) 
"""
"""
#center point sub set

number = [1,2,3,4,5,7]
length = len(number) #7
center_index = (len(number) // 2) #3
sum_left = 0
sum_right = 0

if length%2 == 0:
    print("-1")
else:
    print(number[center_index])
    for n in range(center_index):
      sum_left = sum_left + number[n]
    print (f"Sum of value left side of center is {sum_left}")
    for n in range(center_index+1,length):
      sum_right = sum_right + number[n]
    print (f"Sum of value right side of center is {sum_right}")
"""
"""
#find center

input_list = [1, 5, -5]
index_value = 0

while index_value < len(input_list):
 sum_left = 0
 sum_right = 0
 left_list = input_list[:index_value]
 for num in left_list:
   sum_left = sum_left+num
   
 right_list = input_list[index_value+1:]
 for num in right_list:
    sum_right = sum_right+num

 if sum_left == sum_right:
   print(f"center value is {input_list[index_value]}")
   break;
 index_value = index_value +1
"""

numbers = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8]

doubleTheNumbers = [n * 2 for n in numbers]
oddNumbers = [n for n in numbers if n % 2 != 0]

numbers3 = numbers
numbers3.append(9)
print(numbers3)
print(numbers)
