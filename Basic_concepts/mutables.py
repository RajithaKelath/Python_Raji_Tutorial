

#Integer,float,double,strings,tuple are non-mutable
my_int = 5
print(id(my_int))

my_int = my_int+1 #in backgrd def __add__() is happening
print(id(my_int))

my_int += 1 #in backgrd my_int= my_int.__iadd__(1) is happening
print(id(my_int))

age = 20
def increaseage(current_age):
    current_age = current_age + 1

print(id(age))
increaseage(age)
print(id(age))

primes = ['2','3','5']
print(id(primes))

primes = primes +  ['7','11']  #in backgrd primes= primes.__add__(['7','11']) is happening
print(primes)
print(id(primes))

primes += ['13']  #in backgrd primes= primes.__1add__(['13']) is happening. 
#Its upto the implemenatation of function to decide it will modify or create new memory address
print(primes)
print(id(primes))



#Dictionary, List are mutable
friends_last_seen = {'Rolf':25 ,'Anna': 30}
print(id(friends_last_seen))

friends_last_seen['Rolf'] = 26 #in backgrd def __setitem__() is happening
print(id(friends_last_seen))

#mutability in action:
print('mutability in action')

def lastseen(freinds, name):
    print(id(freinds))
    freinds[name]=0

print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

lastseen(friends_last_seen,'Rolf')
print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))

#Another Common problem

def create_account(name:str, holder:str, account_holders:list = []): #account_holder is created when the function is defined not when it is called
    account_holders.append(holder)
    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders
    }

#a1 = create_account('Current','Rolf')
#a2 = create_account('Savings','Bob')

#print(a2) #Rolf get included even though we ran only for a2

#To solve this, do npt create default list, send empty list 

a3 = create_account('Current','Rolf',[])
a4 = create_account('Savings','Bob',[])

print(a4)

#Argument Unpacking

def print_friends(id:int, name:str):
    print (id,name)

friends = [(0,'a'),(1,'b'),(3,'c')]

for f in friends:
    print_friends(*f) #f[0],f[1] -> *f this will unpack iterables

#Named Argument

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return 'Username is ' + self.username + ' and password is ' + str(self.password)

users = [{'password': 123, 'username': 'Rolf'},
         {'password': 456, 'username': 'Bob'}
         ]

user_object = [print(User(**data)) for data in users] #Unpacking dictionary #If its an named argument order doesn't matter 

users_tuple = [('Rolf',123),
         ('bob', 456)
         ]

user_object_tuple = [print(User(*data)) for data in users_tuple] #Unpacking dictionary

