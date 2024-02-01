import json
import time
import sched
import requests
import telebot
import os
BOT_TOKEN = os.environ.get('BOT_TOKEN')
s = sched.scheduler(time.time, time.sleep)
token = BOT_TOKEN
bot = telebot.TeleBot(token)

def get_links():
    response = requests.post('https://anon4ik-get-furry.hf.space/get_images')
    if response.text:
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            print("Ошибка: ответ не является JSON")
    else:
        print("Ошибка: пустой ответ")
    return []


def send_message(sc):
    links = get_links()
    for link in links:
        bot.send_message(-4157560547, str(link))
        bot.send_photo(-1001908844448, str(link))
    s.enter(3600,1, send_message, (sc,))
s.enter(3600, 1 , send_message, (s,))
s.run()

bot.polling(none_stop=True)
