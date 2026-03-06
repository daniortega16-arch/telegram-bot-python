import os
import telebot
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 PolyBot! /poly = Top value bets")

@bot.message_handler(commands=['poly'])
def poly(message):
    r
