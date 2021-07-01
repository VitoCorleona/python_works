# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:21:09 2021

@author: Toshmurodov Ilkhomjon
"""

info = {"dima":"shitda o'ynaydi","furqat":"disantda o'ynaydi",
        "zafar":"trosda o'ynaydi","dilshod":"nividinka",
        "alijon":"elktro","sunnat":"lazer"}

p = input("Kalit so'z kiriting\n>>>")
print(info.get(p,"Bunday qatnashchi yo'q."))