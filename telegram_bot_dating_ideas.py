import telebot
import os

from random import randint
from telebot import types
from functions import *
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('token_telegram_mark1')
token_vk = os.getenv('token_vk')

compliments = {1: 'Твои губы как легкий утренний бриз',
               2: 'В профиль ты настоящая Клеопатра!',
               3: 'Ты лучше, чем пицца от Pizza Ricco',
               4: 'Ты хорошая хозяйка'}

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_roma = types.InlineKeyboardButton('roma bikmurzin'.title(), callback_data='adam_081')
    button_liza = types.InlineKeyboardButton('Elizaveta Yuretskaya'.title(), callback_data='yuretskaya_liza')
    button_compliment = types.InlineKeyboardButton('Хочу комплимент', callback_data='compliment')
    markup.add(button_roma, button_liza, button_compliment)

    bot.send_message(message.chat.id, 
                     'Кого хочешь проверить?', 
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def feedback_on_welcome_inline(call):
    #bot.send_message(call.message.chat.id, call.message)
    if call.data == 'adam_081':
        user_data_json = extract_dict_from_json(find_user_info(call.data, token_vk))
        bot.send_message(call.message.chat.id, is_user_online(user_data_json))
    elif call.data == 'yuretskaya_liza':
        user_data_json = extract_dict_from_json(find_user_info(call.data, token_vk))
        bot.send_message(call.message.chat.id, is_user_online(user_data_json))
    elif call.data == 'compliment':
        сompliment = compliments(randint(1,5))
        bot.send_message(call.message.chat.id, сompliment)

    #edit inline keyboard
    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text = 'Кого хочешь проверить?', 
                          reply_markup=None)


bot.polling(non_stop=True)