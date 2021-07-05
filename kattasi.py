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




















