"""
def greet():
    print('Hello')


def before_and_after(func):
    print('before...')
    func()
    print('after...\n')


before_and_after(greet)
before_and_after(lambda: 5)
"""

movies = [
    {"Title": "Avatar","Year": "2009","Director": "James Cameron"},
    {"Title": "I Am Legend","Year": "2007","Director": "Francis Lawrence"},
    {"Title": "300","Year": "2006","Director": "Zack Snyder"},
    {"Title": "The Avengers","Year": "2012","Director": "Joss Whedon"} 
]
"""
def find_movie(finder):
    for movie in movies:
        print(finder(movie))

#find_by = input("What property you are looking for? ")
#looking_for = input("What are you looking for? ")
find_movie(lambda movie: movie['Title'])

my_movie = list (map (lambda movie: movie['Title'] , movies))

#print(my_movie)

for movie in movies:
        print (movie['Title'])
        result = lambda movie: movie['Title'](movie)
        print(result)
        
"""

add = lambda x, y: x + y
print(add(2,3))


print((lambda x, y: x + y)(2,3))
