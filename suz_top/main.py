# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:52:10 2021

@author: Toshmurodov Ilkhomjon
"""
import random as r
def play():
    suzlar = ["gilam","qoshiq","vilka","kosa","piyola"]
    suz = r.choice(suzlar)
    chalkash_suz = list(suz)
    r.shuffle(chalkash_suz)
    print (f"Bu qanday so'z: {chalkash_suz}")
    return suz









#javob = input(f"Bu qanday so'z: {chalkash_suz}\n>>>")
#if suz == javob:
   # print(f"Bu haqiqatdan {suz.title()} edi.") 
#else:
    #print("Qayta urinib ko'ring.")
        



































