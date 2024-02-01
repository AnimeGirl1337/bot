from flask import Flask
from flask import request
import time
import requests
from threading import Thread

app = Flask('')

@app.route('/')
def home():
   return ('I am alive')

def run():
  app.run(host='0.0.0.0', port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()
