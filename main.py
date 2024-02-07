import json
import time
import sched
import requests
import telebot
import os
from telebot.types import InputMediaPhoto
from back import keep_alive

BOT_TOKEN = os.environ['BOT_TOKEN']
URL = os.environ['URL']
s = sched.scheduler(time.time, time.sleep)
token = BOT_TOKEN
bot = telebot.TeleBot(token)
keep_alive()
def get_links():
    response = requests.post(URL)
    if response.text:
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            print("Ошибка: ответ не является JSON")
    else:
        print("Ошибка: пустой ответ")
    return []


def send_message(sc):
    try:
        links = get_links()
    except Exception as e:
        return str(e)
    files = []
    try:
        for link in links[:-1]:
            files.append(InputMediaPhoto(media = str(link), caption = str(links[-1])))
            try:
                bot.send_message(-4157560547, str(link))
                bot.send_photo(-1001908844448, str(link))
            except Exception as e:
                bot.send_message(-4157560547, str(e))
    except Exception as e:
        bot.send_message(-4157560547, str(e))
    try:
        bot.send_media_group(chat_id = -1002095649693, message_thread_id = 4, media = files)
    except Exception as e:
        bot.send_message(-4157560547, str(e))
    s.enter(3600,1, send_message, (sc,))
s.enter(3600, 1 , send_message, (s,))
s.run()
