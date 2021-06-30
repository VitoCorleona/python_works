# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:03:37 2021

@author: Toshmurodov Ilkhomjon
"""

print("Welcome to our museum.")
age = int(input("How old are you?"))
if age<=4 or age>=60:
    print("Admission to our museum is free for you.")
elif age<=18:
    print("Admission to our museum is 1$ for you.")
else:
    print("Admission to our museum is 5$ for you.")
