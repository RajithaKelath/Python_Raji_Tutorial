#GIL - Global interpreter Lock

"""
Due to how python is implemented, you cannot run two threads in one process at same time even if you have two core.
Each process in python create a key resource.
when a thread is running, it much acquire that resource
Since there is only one resource, only one thread can run in a process at once.

GIL - is the resource they muct acquire
"""

import time
#from threading import Thread
from concurrent.futures import ThreadPoolExecutor #It will create pool of thread and allow us to execute our functions

def ask_user():
    start_time = time.time()
    user_name = input("Enter your name: ") #Blocking operation, it waste time by waiting for user to type
    greet = f'Hello!, {user_name}'
    print(greet)
    print(f'ask_user time: {time.time() - start_time}')

def complex_calculation():
    start_time = time.time()
    print("Started calculating")
    [x**2 for x in range(20000000)]
    print(f'complex calculation time: {time.time() - start_time}')

#run synchronously
start_time = time.time()
ask_user()
complex_calculation()
print(f'single thread total time: {time.time() - start_time}')

start_thread = time.time()
#run Asynchronously using Thread module

"""
thread1= Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start_thread = time.time()

thread1.start()
thread2.start()

thread1.join() #blocking operation, it will wait till the thread1 complete
thread2.join()
"""

#run Asynchronously using ThreadPoolExecutor  module

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'two thread total time: {time.time() - start_thread}')

#Note: If you kill a thread before releasing GIL, it will be dead locked, bczo next thread is waiting for GIL to release which was killed

