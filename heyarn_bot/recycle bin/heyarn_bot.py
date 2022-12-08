import telebot
from telebot import types

from vsefunkcii import *
from peremennye import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):

        startMsgSend(bot, message)

    @bot.message_handler(content_types=["text", "photo", "sticker"])
    def send_text(message):

        if message.text.lower() == "кискин":
            SendAdmin(bot, message)



        else:
            AskQestions(bot, message)
        
    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)

