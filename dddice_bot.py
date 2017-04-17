#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import telebot
import random


TOKEN = '263341912:AAEFHA5qd1SgStPJkhcBYSCCkZvfjyl7-qA' # полученный у @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, ролевички!')
    
@bot.message_handler(commands=['restart'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет,ролевички!')

@bot.message_handler(commands=['help'])
def help(message):
        sent = bot.send_message(message.chat.id, 'Доступны для броска: d4 d6 d10 d20 d100')


   
@bot.message_handler(regexp = "d20")
def handle_message(message):
    dice20 = random.randint(1,20)
    sent = bot.send_message(message.chat.id, dice20)
    pass

@bot.message_handler(regexp = "d4")
def handle_message(message):
    dice4 = random.randint(1,4)
    sent = bot.send_message(message.chat.id, dice4)
    pass

@bot.message_handler(regexp = "d6")
def handle_message(message):
    dice6 = random.randint(1,6)
    sent = bot.send_message(message.chat.id, dice6)
    pass

@bot.message_handler(regexp = "d100")
def handle_message(message):
    dice100 = random.randint(1,100)
    sent = bot.send_message(message.chat.id, dice100)
    pass


    
bot.polling(none_stop=True)
