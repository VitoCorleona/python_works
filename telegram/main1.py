# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:05:10 2021

@author: Toshmurodov ILhomjon
"""
import random as r
import telebot
from telebot import types
TOKEN = "1867666175:AAHzFzp6AQv-a5rOjWUGnaSMH37RyszQFWc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
tb = telebot.AsyncTeleBot(TOKEN)

son = 0;
pc_son = 0;

@bot.message_handler(content_types=['text'])
def start(message):
    global pc_son
    pc_son = r.choice(range(10,100));
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Bitta son o'yladim. 1dan 10 oralig'ida. TOPING!");
        bot.register_next_step_handler(message, get_number);
    else:
        bot.send_message(message.from_user.id, '/start ni bosing.');

def get_number(message):
    global son;
    son = int(message.text);
    if son > pc_son:
        bot.send_message(message.from_user.id, f'Men o\'ylagan son {son}dan kichikroq.');
        bot.register_next_step_handler(message, get_number2);
    elif son < pc_son:
        bot.send_message(message.from_user.id, f'Men o\'ylagan son {son}dan kattaroq.');
        bot.register_next_step_handler(message, get_number2);
    else:
        bot.send_message(message.from_user.id, f'Men {pc_son}ni o\'ylagandim');
        bot.register_next_step_handler(message, start);
            

def get_number2(message):
    global son;
    son = int(message.text);
    if son > pc_son:
        bot.send_message(message.from_user.id, f'Men o\'ylagan son {son}dan kichikroq.');
        bot.register_next_step_handler(message, get_number);
    elif son < pc_son:
        bot.send_message(message.from_user.id, f'Men o\'ylagan son {son}dan kattaroq.');
        bot.register_next_step_handler(message, get_number);
    else:
        bot.send_message(message.from_user.id, f'Men {pc_son}ni o\'ylagandim');
        bot.register_next_step_handler(message, start);
            
bot.polling()      