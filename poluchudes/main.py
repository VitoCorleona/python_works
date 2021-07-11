# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:01:07 2021

@author: Toshmurodov Ilkhomjon
"""

from uzwords import words
import random as r

def get_words():
    suz = r.choice(words)
    return suz

def display(suz,hariflar):
    javob = []
    if suz:
        for n in suz:
            if n in hariflar:
                javob.append(n)
            else:
                n="_"
                javob.append(n)
    print(" ".join(javob).upper())
    return javob

def play():
    input("O'yinni boshlash uchun \"Enter\"ni bosing:")
    suz = get_words()
    andoza = list(suz)
    harflar = []
    ans = True
    while ans:        
        javob = display(suz,harflar)
        if javob == andoza:
            harflar =[]
            suz = get_words()
            ans = input("Yana o'ynaysizmi? (Ha) 1,(Yo'q) 0:")
        if ans == "0":
            ans = False
        print (suz)# olib tashlansiz
        harf = (input("Harf kiriting:").lower())
        if harf not in harflar:
            harflar.append(harf)
            print(f"Siz kiritgan hariflar: {', '.join(harflar).upper()}")
        elif harf in harflar:
            print(f"{harf.upper()} harfini oldin kirgizgansiz.")                
        
            
play()                
