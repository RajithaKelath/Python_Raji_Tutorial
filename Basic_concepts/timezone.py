from datetime import datetime, timezone, timedelta

print(datetime.now())
print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)
print(today.strftime('%d-%m-%Y %H:%M:%S'))

import time

def measures(func): #decorator function
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def powers(limit):  #first class function
    return [x**2 for x in range(limit)]

measures(lambda: powers(5000000))

import timeit #execute the statement like in shell script for sql

print(timeit.timeit("[x**2 for x in range(100)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(100)))"))

