# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:33:06 2021

@author: Toshmurodov Ilkhomjon
"""

import random as r
        
def son_top_pc(x=10):            
    input ("Son o'ylagan bo'lsangiz 'Enter'ni bosing.")
    quyi = 1
    yuqori = x
    taxminlar=0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'ylagan edingiz."
                      f"To'g'ri (t), Men oylagan bundan kattaroq bo'lsa (+)"
                      f"yoki kichikroq bo'lsa (-):".lower())
        if javob == "+":
            quyi = taxmin + 1
        elif javob == "-":
            yuqori = taxmin - 1
        elif javob == "t":
            break
    print (f"{taxminlar}ta urinishda topdim.")
    return taxminlar
      
def son_top(x=0):
    n=0
    son = list(range(1,11))
    x = r.choice(son)
    print("Keling o'ylagan sonni topish o'ynaymiz!")
    a = int(input("1 dan 10 gacha bo'lgan son o'yladim topa olasizmi?:\n>>"))
    while True:
        n=n+1
        if a>x:
            a = int(input("Xato, men o'yalgan son kichikroq."
                          "Yana urinib ko'ring:\n>>"))
        elif a<x:
            a = int(input("Xato, men o'yalgan son kattaroq."
                          "Yana urinib ko'ring:\n>>"))
        elif a==x:
            print(f"Topdingiz! men {x} sonini o'ylagan edim."
                  f"Siz {n} ta taxmin bilan topdingiz.")
            break
    return n
    
def play(x=10):
    yana = True
    while yana:
        taxminlar_player = son_top(x)
        taxminlar_pc = son_top_pc(x)
        if taxminlar_player > taxminlar_pc:
            print(f"Siz {taxminlar_player}-u {taxminlar_pc}ga yutdingiz.")
        elif taxminlar_player < taxminlar_pc:
            print(f"Men {taxminlar_player}-u {taxminlar_pc}ga yutdim.")
        elif taxminlar_player == taxminlar_pc:
            print(f"{taxminlar_player}-u {taxminlar_pc}ga durrang.")
        yana = input("Yana o'ynaysizmi.(Ha)=1 yoki (Yo'q)=0:\n>>>")
    if yana == 0:
        print("Maroqli o'yin uchun raxmat.")
    return yana
        
            
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

        




        
        
        






