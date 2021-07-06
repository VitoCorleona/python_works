# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 22:17:14 2021

@author: Toshmurodov Ilkhomjon
"""

def kattasi(a,b,c):
    max = a
    if b>max:
        max = b
    if c>max:
        max = c
    return max

num3 = []
a = input('a:')
b = input('b:')
c = input('c:')
num3.append(kattasi(a,b,c))
print(num3)

def info_circle(radius,pi=3.14159):
    circle = {"radius":radius,
          "diometr":2*radius,
          "peremetr":2*radius*pi,
          "face":pi*radius**2}
    return circle

print(info_circle(50))

def tup_number(min,max):
    number = []
    for num in range(min,max+1):
        tup = True
        if(num==1):
            tup = False
        elif(num==2):
            tup = True
        else:
           for x in range(2,num):
                           if(num%x==0):
                                   tup = False
        if tup:
            number.append(num)
    return number
        
print(tup_number(1,13))

def fibonacci(num):
    numbers=[]
    for n in range(num):
        if n==0 or n==1:
            numbers.append(1)
        else:
            numbers.append(numbers[-1]+numbers[-2])
    return numbers

print(fibonacci(20))

def katta_qil(matnlar):   
    for x in range(len(matnlar)):
        matnlar[x] = matnlar[x].capitalize()
    return matnlar

matn = ["men bozorga bordim.","ko'chada o'ynadim.","gul ekdim."]
print(katta_qil(matn))

def katta_qil(matnlar):
    matnlar = matnlar[:]
    for x in range(len(matnlar)):
        matnlar[x] = matnlar[x].capitalize()
    return matnlar

matn = ["men bozorga bordim.","ko'chada o'ynadim.","gul ekdim."]
print(katta_qil(matn))
print(matn)

def bahola(ismlar):
    isml = ismlar[:]
    baholar = {}
    for ism in isml:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)

def kopaytir(*son):
    num = 1   
    for n in son:
        num *= n
    return num

print(kopaytir(5,6,7,8,9,7))

















