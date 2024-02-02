import json
import time
import sched
import requests
import telebot
import os
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
    for link in links:
        bot.send_message(-4157560547, str(link))
        bot.send_photo(-1001908844448, str(link))
    s.enter(50,1, send_message, (sc,))
s.enter(50, 1 , send_message, (s,))
s.run()
