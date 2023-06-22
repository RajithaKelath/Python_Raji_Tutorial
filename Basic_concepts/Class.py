"""
class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade
        
    def student_avg(self):
        return (f"<<{self.name}>> by {self.grade}")

student_one = Student("The Matrix" , "Wachowski")
print(student_one.student_avg())
"""
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, name):
        super().__init__(max_speed, mileage)
        self.name  = name

    def __repr__(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"

modelX = Bus(180, 12, "School Volvo")
print(modelX)
"""
"""
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

school_bus = Bus("School Volvo", 180, 20)
print(school_bus.seating_capacity())
"""
"""
class Vehicle:
    #class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

"""
"""
#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        return super().fare() + (0.1 * super().fare()) 

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
"""
"""
#Write a program to determine which class a given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus)) #or print(School_bus.__class__)
"""
"""
#Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Bus))

"""

#Python program to build flashcard using class in Python

#Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.

class Flashcard:
     flash = []

     def __init__(self, word, meaning):
          self.word = word
          self.meaning = meaning

    #Now we use the __str__() function to return a string that contains the word and meaning.

     def __str__(self):
          return self.word + ' ( ' + self.meaning + ' ) '
             

def main_program():

    flash = []

    #Take the word and its meaning as input from the user.
    user_word = input("Enter the word: ")
    user_meaning = input("Enetr the meaning: ")

    #Store the returned strings in a list named flash.
    flash.append(Flashcard(user_word,user_meaning))

    #print all the stored flashcards
    for i in flash:
         print(i)


main_program()