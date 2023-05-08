import telebot
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from functions_file import value_plus_one, pstat, obnulenie_stat, ball_of_fate, Davinci, Artur
from paswords import *

token = lemonade

bot = telebot.TeleBot(token)