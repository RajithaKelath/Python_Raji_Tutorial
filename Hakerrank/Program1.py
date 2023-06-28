#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task 1
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""

def odd_or_even():
    if n % 2 != 0:
        print("Weird")
    elif n in range(2,5):
        print("Not Weird")
    elif n in  range(6,21):
        print("Weird")
    elif n > 20:
        print ("Not Werid")
"""
Task2
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
def calculation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a/b)

"""
Task 3
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n , print .
"""
def square_n(n):
    for i in range (n):
        print (i**2)

"""
Task4
In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
"""
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    
    return leap

def seq_num(n):
    previous = ''
    for i in range(1, n+1):
        current = i
        previous = previous + str(current)

    print(previous)

if __name__ == '__main__':
    #Task1
    #n = int(input().strip())
    #odd_or_even()

    #Task2
    #a = int(input())
    #b = int(input())
    #calculation(a,b)

    #Task3
    #n = int(input())
    #square_n(n)

    #Task4
    #year = int(input())
    #print(is_leap(year))  #sample leap year = 2000,2400, 2012 non-leap year = 2300, 1900

    #Task5
    n = int(input())
    seq_num(n)
