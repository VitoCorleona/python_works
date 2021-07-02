# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:14:46 2021

@author: Toshmurodov Ilkhomjon
"""
name = input("What is your name?\n>>>")
books = []
num = 1
question = ()
while True:
    answer = input(f"Hello {name.title()}.\n\
{num}-What is your favourite book\n\
If :>>>")
    num = num + 1    
    if answer == "stop":
        break
    else:
        books.append(answer)
print("Thanks they are your favourite books;")
for n in books:
    print(n)