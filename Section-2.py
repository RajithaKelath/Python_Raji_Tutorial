#if else statement
friends = ["Jenny", "Charlie", "Bob"]
family = ["Ram", "Sita"]

user_name = input("Enter your nam2e: ")

if user_name in friends:
  print("Hello Friend!")
elif user_name in family:
  print("Hello Family!")
else:
  print("Hello stranger")
