"""
#Enumerate : when dealing with iterators, we also get need to keep a count of iteration

friends = ["Rolf" , "Bod", "Anne"]

for counter, friend in enumerate(friends , 1):
  print(counter, friend)

print(list(enumerate(friends)))

#Zip will concatenate both list
print(list(zip([1,2,3],friends)))

numbers = [1,2,3,4,5]
new_number = [n for n in numbers]

print(new_number)
"""

#Sample program to find winner of lottery
import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]
new_list= []

for num in range(len(players)):
    new_list.append((players[num]["name"],len(lottery_numbers.intersection(players[num]["numbers"]))))

top_name=new_list[0][0]
top_amount=new_list[0][1]

for num in range(len(new_list)):

  if new_list[num][1] > top_amount:
    top_name = new_list[num][0]
    top_amount = new_list[num][1]

print(f"{top_name} won {100 ** top_amount}.")


"""
#Functions

def add(x=0, y=3):
  total = x + y
  return total

print(add(y=5))

"""
"""
#Lamba


def divide(x, y):
  return x / y


#similar to lambda - If no names(divide_lam) assigned to it, it will not be stored and destroyed once executed

divide_lam = lambda x, y: x / y

print(divide_lam(15, 3))
"""