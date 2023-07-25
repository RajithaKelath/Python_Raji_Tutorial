"""
stack = [0, 9, 2 , 3 , 1]

def add(a , x):
    a.append(x)
def remove(a):
    a.pop()

add(stack,5)
add(stack,6)
print(stack)
remove(stack)
print(stack)

from collections import deque

deque_list = deque(['a','b','c','d'])
deque_list.append('e')
deque_list.append('f')
print(deque_list)
deque_list.popleft()
print(deque_list)
"""

x1 = {1:'a', 2:'b', 3:'a'}
project = {
        'id' : '1',
        'title' : 'Ecommerce website',
        'description' : 'Fully functional E-comm website'
    }
#print(project['id'])
#project.id

#print(x1.items())


#print( '---'.join(['foo', str(23), 'bar']))
#print( '---'.join([1,2,3]))

#print((lambda x : x**2)(5))
#print((lambda a , b:f'Sum of {a} and {b} is {a+b}'))
"""
def swap_case(s):
    return (s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
"""
""" 
def print_full_name(first, last):
    # Write your code here
    print (f'Hello {first} {last}! you are delved into python')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
"""
"""
def count_substring(string, sub_string):
    count = 0
    n=0
    p = len(sub_string)
    while n <= (len(string)-p):
        if string[n:n+p] == sub_string:
            count += 1
        n += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
"""

     # Create a sequence of data
grades = [{'name': 'Jennifer', 'final': 95},
        {'name': 'David', 'final': 92},
        {'name': 'Aaron', 'final': 98}]

list = [1,5,2,3,7,11,0]
#sort grades based on name
#print(sorted(grades,key=(lambda x : x['name'])))
#print(sorted(list))

#print(chr(ord('a')+3))


"""
#fibonacci series
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
current = 1
previous = 0
n = 0

fibo_series = [0,1]

upto = int(input('Enter num: ' ))
n = 1
while n < upto:
    num = current + previous
    fibo_series.append(num)
    previous = current
    current = num
    n += 1

print(fibo_series)
"""

#Factorial
def recursive(x):
    '''This is a function to return factorial of integer'''

    if x == 1:
        return x
    else:
        return ( x * recursive(x-1))
    
num = int(input())    
print(f'The factorial of number {num} is {recursive(num)}!')