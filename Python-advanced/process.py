"""
Multiprocessing in Windows or ARM Macs

-Due to the way these systems work you must make sure that the code that starts a process is surrounded by if __name__ == "__main__".
-Otherwise when we start new processes, those processes automatically start new processes, and those start new ones, and so on.
-Python will not allow this to happen, and as protection it requires the above if statement.
"""

import time
from multiprocessing import Process
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
print(f'single process total time: {time.time() - start_time}')

#run Asynchronously
start_thread = time.time()

if __name__ == '__main__':
    process = Process(target=complex_calculation)
    process.start()

    start = time.time()

    ask_user()

    process.join()

    print(f'Multi process total time: {time.time() - start}')

