"""
*Counter
*defaultdict
*orderdict
*Named tuple
*deque
"""
"""
#counter

from collections import Counter
my_list = [1,1,1,2,2,3,3,2,4,4,4,5,6,7]

print(Counter(my_list)[5])

#defaultdict
from collections import defaultdict
coworkers = [('Rolf','MIT'), ('Bob','Cambridge'),('Rolf','Oxford')]

data_dict = {}

for coworker, place in coworkers:
    if coworker not in data_dict:
        data_dict[coworker] = []
    data_dict[coworker].append(place)

print(data_dict['Rolf'])
#print(data_dict['Anne']) #KeyError: 'Anne' throw error

#instead use data dict

data_dict_default = defaultdict(list) #defaultdict takes only funcation as argument, so pasisng list fun

for coworker,place in coworkers:
    data_dict_default[coworker].append(place)

print(data_dict_default['Rolf'])
print(data_dict_default['Anne']) #create empty list


#use defauly company

my_company = 'Teclado'

my_cowrker = ['Jen','Bob','Joseph']
other_coworkers = [('Rolf','Apple Inc'), ('Anne','Google')]

coworkers_list = defaultdict(lambda: my_company) #It takes only funcation as argument as passing lambda

for coworker, place in other_coworkers:
    coworkers_list[coworker] = place


print(coworkers_list[my_cowrker[0]])
print(coworkers_list['Jen'])
print(coworkers_list['Anne'])
print(coworkers_list['Joseph'])

#Named tuple
from collections import namedtuple
#account = ('savings',1837.50)

Account = namedtuple('Account',['name','balance']) #it will create name for tuples
account = Account('savings',1837.50)

print(account)


#deque - add and remove items from both end #Can used to add in tuple
from collections import deque

friends = ('Rolf','Anne','Bob')
add_friend = deque(friends)

add_friend.append('Jen')
add_friend.appendleft('Raji')
print(add_friend)

add_friend.pop()
add_friend.popleft()
print(add_friend)

"""

from collections import defaultdict, OrderedDict, namedtuple, deque


arg_od = OrderedDict([
    ('Alan', 'Manchester'),
    ('Bob', 'London'),
    ('Chris', 'Lisbon'),
    ('Dan', 'Paris'),
    ('Eden', 'Liverpool'),
    ('Frank', 'Newcastle')
])

def task2(arg_od: OrderedDict):
    arg_od.pop('Frank')
    arg_od.pop('Alan')
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan' , last = False)


task2(arg_od)
print(arg_od)

def task1() -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    # you code starts here:
    d = defaultdict(lambda: 'Unknown')
    d['Alan'] = 'Manchester'
    return d

person = task1()
print(person['Alan'])
print(person['Bob'])

def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:
    Player = namedtuple('Player',['name','club'])
    return Player

player = task3('Raji','Manchester')
print(player('Raji','Manchester'))
print(player('Paranv','MNC'))

my_list = ('Bob','Anne','David','Rahul')
arg_deque = deque(my_list)

def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    arg_deque.pop()
    arg_deque.rotate(-1)
    arg_deque.extendleft(['Zack'])

print(arg_deque)
task4(arg_deque)
print(arg_deque)