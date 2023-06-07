
"""
#Raising error in python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<Car {self.make} {self.model}>"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_cars(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tries to raise {car.__class__.__name__}, we can raise only car object")
        self.cars.append(car)

    
ford = Garage()
car = Car("Ford","Fiesta")
ford.add_cars(car)
print(len(ford))

"""

"""
for the function below, add your code in appropriate place that checks the input n.
n should be a non-negative integer, otherwise a ValueError should be raised
and a proper error message should be provided informing the user of the error
for simplicity, you may assume that the input is always an integer for this exercise

def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError("n should be a positive value")

    for x in range(0, n+1):
        print(x)
    
count_from_zero_to_n(-2)

"""
"""

class MyCustomeError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

raise MyCustomeError("Oouch! There is an error", 500)
"""
"""
class UncountableError(ValueError):
    def __init__(self,wrong_value):
        super().__init__(f"Invalid value for n, {wrong_value} be greater than 0.")
        

# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way

def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)

count_from_zero_to_n(-2)
"""

#try-except-else-finally
def interact():
    while True:  # keep looping until user reach break statement
    
        try:
            user_input = int(input('Please input an integer:'))     # turn the user input into an integer
            
        except ValueError:
            print('Please input integers only.')
        
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print out the message '{user_input} is {even/odd}.'
        
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit