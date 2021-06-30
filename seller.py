# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:32:07 2021

@author: Toshmurodov Ilkhomjon
"""

products = ["oil","water","carrot","potato","tomato","chocolat","onion","coffe","banana"]
costumer = []
print('Please enter 5 products.')
n=1
while n <= 5:
    costumer.append(input(f"{n} What would you like from our market?\n>>>"))
    n+=1

if costumer:
    for demand in costumer:
        if demand in products:
            print(f"There is {demand} in our shop.")
        else:
            print(f"There isn't {demand} in our shop.")

       