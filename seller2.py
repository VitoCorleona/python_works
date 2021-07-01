# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:24:43 2021

@author: Toshmurodov Ilomjon
"""

products = ["apple","apricot","potato","oil","tomato","cucumber","onion","carrot"]

pacet = []
for n in range(1,6):
    pacet.append(input(f"{n} Enter products in pacet:\n>>>"))
if pacet:
    for buy in pacet:
        if buy in products:
            print (f"There is {buy} in our shop")
        else:
            print (f"There isn't {buy} in our shop")
y = []
s = []            
if pacet:
    for buy in pacet:
        if buy in products:
            y.append(buy)
            
        else:
            s.append(buy)                       
for u in s:
    print(f"There aren't {u} in our shop.") 
for k in y:
    print(f"There are {k} in our shop.")            