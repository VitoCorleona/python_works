# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:48:20 2021

@author: Toshmurodov Ilkhomjon
"""

users = ["dima","max","jhon","stive","vito"]
login = input("Enter your login:\n>>>")

if login in users:
    print("This login is already busy")
else:
    users.append(login)
    print(f"{login.title()}. Welcoma to our wepside")