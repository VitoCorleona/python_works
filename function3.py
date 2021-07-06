# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:15:29 2021

@author: Toshmurodov Ilkhomjon
"""

def kopaytir(*son):
    num = 1   
    for n in son:
        num *= n
    return num

print(kopaytir(5,6,7,8,9,7))   

def list_tuz(name,surname,**ad_info):
    ad_info["name"]=name
    ad_info["surname"]=surname
    return ad_info

print(list_tuz("Ilhomjon","Toshmurodov",yosh=32,tel=902642731))