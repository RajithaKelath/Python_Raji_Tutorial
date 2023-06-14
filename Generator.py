#Iterator : Used to get next value
#Iterable : Used to go over all the values of iterator

"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""
"""
def prime_number(bound : int):
    # your code starts here (delete the pass):
    for n in range(2,bound):
        for num in range(2,n):
            if n % num == 0:
                break
        else:
            print(f'{n} is a prime number')

def prime_generator(bound : int):
    # your code starts here (delete the pass):
    for n in range(2,bound):
        for num in range(2,n):
            if n % num == 0:
                break
        else:
            yield n

g = prime_generator(15)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


#Define a class that act as Generator and catch StopIteration error:

class FirstFiveGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 5:
                current = self.number
                self.number += 1           
        else:
            raise StopIteration
        
        return current

my_gen = FirstFiveGenerator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
"""

"""
# Define a PrimeGenerator class

class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.x = 2
        self.y = 1

    def __next__(self):
        if self.x < self.stop:
            self.y = 1
            while self.y < self.x:
                if self.x % self.y == 0:
                    break
                else:
                    self.y += 1
                
                return (self.x)
            
            self.x += 1

my_gen = PrimeGenerator(9)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
"""

class PrimeGenerator():
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.y = 2

    def __next__(self):
        for n in range(self.y, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.y += 1
                return n
            self.y += 1
        raise StopIteration
                
my_gen = PrimeGenerator(11)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


class PrimeIterator:
    def __iter__(self):
        return PrimeGenerator(11)
    
for i in PrimeIterator():
    print(f'New iterabale item: {i}')


class AnotherIterable: #If a class has both length and getitem dunder method, then without __next__ or __iter__ it can be treated as iterable
    def __init__(self):
        self.cars = ['Ford','BMW']

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,i):
        return (self.cars[i])

for car in AnotherIterable():
    print(car)



#Filter function will filter values and act as generator

friends = ['Rolf','Jose','Randy', 'Bob', 'Anna','Raji']

my_friend_filter = filter(lambda friend: friend.startswith('R'), friends)

print(list(my_friend_filter))

my_friend_lower = map(lambda friend: friend.lower(), friends) #map will map function to list of items
print(next(my_friend_lower))
print(next(my_friend_lower))

#any function check if any value sets TRUE
my_list = [0,0,0,0,1]

if any(my_list):
    print('There is some True')
else:
    print('All are False')

#all function check if all value sets TRUE
my_next_list = [1,1,1,1,0]

if all(my_next_list):
    print('All are True')
else:
    print('There is some Flse')

#__bool__magic method will override bool function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True


if __name__ == '__main__':
    person = Person('Jane', 16)
    print(bool(person))  # False