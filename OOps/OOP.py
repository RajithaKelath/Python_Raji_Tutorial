class Vehicle:
    def __init__(self,type, name,colour,wheel):
        self.type = type
        self.name = name
        self.colour = colour
        self.wheel = wheel

    def __str__(self):
        return (f'This is a {self.type} object Name: {self.name}, colour: {self.colour}, wheel: {self.wheel}')

car = Vehicle('Car','ford','red',4)
bike = Vehicle('Bike','Suzuki','white',2)
auto = Vehicle('Auto','Tata','Yellow',3)

# print(id(Vehicle))
# print(id(car))
# print(id(bike))
# print(id(auto))


# tuple_list = ("5.4" , "Radio" , 7)

# constructor_tuple = tuple(["5.4" , "Radio" , 7 , tuple_list])
# print(type(constructor_tuple))

# first = list(tuple_list)
# print(id(first))
# first.append('newly_added')
# tuple_list = tuple(first)
# print(tuple_list)
# print(id(tuple_list))

# print(constructor_tuple)
# #unpacking
# second , third , *rest = constructor_tuple
# print(second,third,rest)
# print(type(second))
# print(type(rest))

# x = 5
# print(id(x))

# def fun():
#     global x
#     x += 4
#     print(x)

# fun()
# print(x)
# print(id(x))


#Class Method and Instance Method

class Student:

    #class attribute
    college = 'Saveetha Engg'

    #Instance attribute
    def __init__(self,sem1,sem2,sem3):
        self.sem1 = sem1
        self.sem2 = sem2
        self.sem3 = sem3

    #return attribute of class
    def __getattr__(self, attr):
        return f"';Student' object has no attribute '{attr}'"

    #Instance method
    def avg(self):
        return (self.sem1 + self.sem2 + self.sem3)/3
    
    @classmethod
    def get_college(cls):
        print (cls.college)
    

std1 = Student(10,20,30)
std2 = Student(50,60,70)
print(std1.total)
print(std1.sem1)

# print(std1.sem1)
# print(Student(20,20,30).sem1)

# print(std1.avg())
# print(Student(10,20,30).avg())
# # print(Student.avg())

# std1.get_college()
# Student(10,20,30).get_college()
# Student.get_college()

#Tuple Unpacking
# old_tuple = (1,2)
# print(old_tuple)
# print(id(old_tuple))
# first,second = old_tuple
# first += 2
# old_tuple = (first,second)
# print(old_tuple)
# print(id(old_tuple))
# print(type(old_tuple))
