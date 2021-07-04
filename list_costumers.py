# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 10:58:45 2021

@author: Toshmurodov Ilkhomjon
"""

def list_costumers(name,surname,birth_y,birth_p,email,tel=''):
    """A return function in the form of a dictionary that takes the user's name,
surname, year of birth, place of birth, email address and phone number.
There is also a user age in the dictionary. It is optional to enter some 
arguments (for example, phone number, e-mail)"""
    l_cos = {'ism':name,
             'familya':surname,
             't_yil':birth_y,
             't_joy':birth_p,
             'yosh':2021-birth_y,
             'email':email,
             'telefon':tel
             }
    return l_cos

print("Mijozlar ro'yxatini kiriting.")
costumers = []
while True:
    ism = input("What is his\her name?\n>>>")
    familya = input("What is his\her surname?\n>>>")
    t_yil = int(input("His\her birth year.\n>>>"))
    t_joy = input("His\her birth place.\n>>>")
    email = input("His\her email.\n>>>")
    telefon = input("His\her tel number.\n>>>")
    costumers.append(list_costumers(ism,familya,t_yil,t_joy,email,telefon))
    door = input("Do you want to stop:yes\no")
    if door!='yes':
        break
print("List of Costumers")
for m in costumers:
    print(f"{m['ism'].title()} {m['familya'].title()} yoshi {m['yosh']},\
{m['t_yil']} {m['t_joy'].title()}da tug'ilgan.Uning emaili {m['email']} \
 telefon raqami {m['telefon']},")













