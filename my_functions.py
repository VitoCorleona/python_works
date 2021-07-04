# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:39:18 2021

@author: Toshmurodov Ilkhomjon
"""

def my_info(name, age):
    """A function that asking username and age,
 calculates the year of his birth."""
    print(f"Hello {name.title()}. You were born in {2021-age}")
    
def num_info(number):
    """A function that takes a number from a user and 
displays its square and cube on the console.""" 
    print(f"{int(number)**2},{int(number**3)}")

def even(number):
    """A function that takes a number from a user and 
outputs an even or odd number to the console."""
    if number%2:
        print(f"{int(number)} odd number.")
    else:
        print(f"{int(number)} is even number.")
        
def w_big(num1,num2):
    """A function that takes two numbers from the user and outputs the 
largest of them to the console. If the numbers are equal, 
it displays the message "Numbers are equal"."""
    if num1>num2:
        print(f"{num1}>{num2}")
    elif num1<num2:
        print(f"{num1}<{num2}")
    else:
        print(f"{num1}={num2}")
           
def x_2(x,y=2):
    """Take the numbers x and y from the user and x
The function that brings y to the console."""
    print(f"{x}**{y}={x**y}")    

def division(x):
    """A function that takes a number from a user and 
checks that the number is divisible by 2 to 10 without 
a remainder. Outputs the results to the console."""
    n = list(range(2,11))
    for m in n:
        if x%m==0:
            print(f"{x} is divisible by {m} indefinitely.")
        else:
            print(f"{x} is not divisible by {m} indefinitely.")
















