# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:33:06 2021

@author: Toshmurodov Ilkhomjon
"""

        
def son_top_pc(Enter):
    import random as r        
    m=0
    ch=1
    sonlar =  list(range(1,11))       
    while True:                        
        m=m+1
        son = r.choice(sonlar)        
        ans = input(f"Siz {son} sonini o'yladingiz: To'g'ri(t),\n\
men oylagan sondan kattaroq (+) yoki kichikroq (-):")
        if ans =='+':
            a=son-ch
            del sonlar[0:a]
        elif ans == '-':
            a=son-ch
            del sonlar[a:-1]            
        elif ans == "t":
           break
    return m

def son_top(son1):
    n=0
    import random as r
    son = list(range(1,11))
    x = r.choice(son)
    print("Keling o'ylagan sonni topish o'ynaymiz!")
    a = int(input("1 dan 10 gacha bo'lgan son o'yladim topa olasizmi?:\n>>"))
    while True:
        n=n+1
        if a>x:
            a = int(input("Xato, men o'yalgan son kichikroq. Yana urinib ko'ring:\n>>"))
        elif a<x:
            a = int(input("Xato, men o'yalgan son kattaroq. Yana urinib ko'ring:\n>>"))
        elif a==x:
            print(f"Topdingiz! men {x} sonini o'ylagan edim. \
Siz {n} ta taxmin bilan topdingiz.")
            break
    return n
jor = True
while jor:
    a=input("Son topish o'yin o'ynaysizmi 'Enter'ni bosing.")
    n=(son_top(a))
    m=(son_top_pc(input("Son o'ylagan bo'lsangiz 'Enter'ni bosing:")))
    if n<m:
        ques=input(f"Siz {n}ga {m} hisob bilan yutdingiz.\
Yana o'ynashni hohlaysizmi?(Ha)yoki(Yo'q):")
    else:
        ques=input(f"Siz {n}ga {m} hisob bilan yutqazdingiz.\
Yana o'ynashni hohlaysizmi?(Ha)yoki(Yo'q):")
    if ques=="Ha":
        jor = True
    elif ques=="Yo'q":
        break

        
        

        




        
        
        






