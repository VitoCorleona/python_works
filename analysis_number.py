# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:20:30 2021

@author: Toshmurodov Ilkhomjon
"""

print("Hello my friend")
x = int(input("Enter first number."))
y = int(input("Enter second number."))
if x<y:
    print(f"{x}<{y}")
elif x>y:
    print(f"{x}>{y}")
else:
    print(f"{x}={y}")