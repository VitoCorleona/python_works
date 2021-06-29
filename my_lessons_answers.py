
"""
Created on Mon Jun 28 20:43:41 2021

@author: Toshmurodov Ilkhomjon
"""

# 1_lesson
print ("Hello world")
print(5*4)
print(5+9)
print(20/5)

# print (Good morning!) #it is false

# 2_lesson
matn = '"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas'
print(matn)
print(5**4)
print(22%4)

# 3_lesson
a = float(input("Enter size of square:\n>>>"))
print(a,"sm which the sides of square.\n\
The surface of square is",a*a,"\n\
The peremetr of square is",a*4)

# 4_lesson task 1
c = input("What is your name?" )
b = int(input(c.title()+". How old are you? "))
print("You were born in",2021-b )

# task 2
k = float(input("Enter some number.\n>>>"))
print(f"the {k}'s square is {k**2} and cobe is {k**3}")

# task 3
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))
print(f"{num_1}+{num_2}={num_1+num_2}\n\
{num_1}-{num_2}={num_1-num_2}\n\
{num_1}/{num_2}={num_1/num_2}\n\
{num_1}*{num_2}={num_1*num_2}")

# 5_lesson task 1
friends = ['Dima','Maqsud','Max','Jahongir','Rustam','Xurshid']
for sms in friends:
    print("Hello "+sms+". How are you?\n"+sms+". Would you like going to football")

#task 2
h_people = ['Napalyon','Enshteyn','Nuyton','Stive Jobs']
l_people = ['Tramp','Putin','Bill Gets','Jeki Chan','Tom Croese']
print(f"I would like to talk with {h_people[-1]} from history people,\n\
from live people {l_people[3]}")

