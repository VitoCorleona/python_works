# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:14:46 2021

@author: Toshmurodov Ilkhomjon
"""
name = input("What is your name?\n>>>")
books = []
num = 1
question = ()
print(f"Hello {name.title()}.")
while True:
    answer = input(f"{num}-What is your favourite book:\n\
(if you want to stoped that write 'stop')>>>")
    num = num + 1    
    if answer == "stop":
        break
    else:
        books.append(answer)
print("Thanks. they are your favourite books;")
for n in books:
    print(n.title())