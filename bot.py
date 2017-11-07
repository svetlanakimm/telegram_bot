# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Котик', 'Лисичка', 'Собачка')
    markup.row('Уточка', 'Мышка', 'Коровка')
    bot.send_message(message.chat.id, "Привет! Выбери животное и узнай что оно говорит", reply_markup=markup)



@bot.message_handler(content_types=["text"])
def handle_continue(message):
    if ((message.text == 'Котик') or (message.text == 'котик')):
        bot.send_message(message.from_user.id, "Котик говорит: «Мяу!»")
    elif ((message.text == 'Лисичка') or (message.text == 'лисичка')):
        bot.send_message(message.from_user.id, "Лисичка говорит: «%;?!»")
    elif ((message.text == 'Собачка') or (message.text == 'собачка')):
        bot.send_message(message.from_user.id, "Собачка говорит: «Гав!»")
    elif ((message.text == 'Уточка') or (message.text == 'уточка')):
        bot.send_message(message.from_user.id, "Уточка говорит: «Кря!»")
    elif ((message.text == 'Мышка') or (message.text == 'мышка')):
        bot.send_message(message.from_user.id, "Мышка говорит: «Пи-пи-пи!»")
    elif ((message.text == 'Коровка') or (message.text == 'коровка')):
        bot.send_message(message.from_user.id, "Коровка говорит: «Муу!»")
    else:
        bot.send_message(message.from_user.id, "Извини, неправильное животное")


if __name__ == '__main__':
     bot.polling(none_stop=True)
