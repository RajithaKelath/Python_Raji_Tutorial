#Ask user for the list of 3 friends
get_friends = []

for n in range(1,4):
    user_friend = input("Enter firend name {}: ".format(n))
    get_friends.append(user_friend)


#Read people file and get list of people
get_people = open("c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/people.txt" , "r")
people_list = get_people.read().splitlines()
get_people.close()

#For each friend we will tell the user wheather he is nearby
get_friends_set = set(get_friends)
people_list_set = set(people_list)
nearby_friend = get_friends_set.intersection(people_list_set)
nearby_friend_list = list(nearby_friend)
print(nearby_friend_list)
#For each nearby friend we will save their name in nearby_people file
write_nearby_people = open("c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/nearby_people.txt" , "w")

for friend in nearby_friend_list:
    write_nearby_people.writelines(f"{friend} " + "\n")

write_nearby_people.close()


#hint : readlines()