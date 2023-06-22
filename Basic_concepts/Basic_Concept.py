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
"""

#Joins
friend = ["Ram" , "Sita", "Vishnu"]
comma_separator = ", ".join(friend)
print(f"My friends are {comma_separator}.")