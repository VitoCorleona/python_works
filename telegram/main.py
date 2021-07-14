# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:30:40 2021

@author: Toshmurodov ILkhomjon
"""
from uzwords import words
import random as r
import telebot
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
            
TOKEN = "1867666175:AAHzFzp6AQv-a5rOjWUGnaSMH37RyszQFWc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
tb = telebot.AsyncTeleBot(TOKEN)

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Ismingiz nima?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Familyangiz nima?');
    #bot.register_next_step_handler(message, get_surnme);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message,'Necha yoshdasiz?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
             bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

  
bot.polling()
