#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from flask import Flask
from flask import request

app = Flask(__name__)

ACCOUNT_SID = 'ACcefa2306ccdba981522a00c621e602ab'
AUTH_TOKEN = 'ba3216346af36cf72ad0fb48e45e5b8e'
PHONE = '+41794477448'
CUSTOMER = '+5491160190584'

JOB_REQUEST = """لقد وجدنا فرصة عمل تناسبك!
المكان: منطقة كوجاتيبي، شارع مختار بيك، بناء رقم ١-٢٠١ / اسطنبول، تركيا
Kocatepe Mahallesi, Şht. Muhtar Bey Cd. No:1, 201 Beyoğlu/İstanbul, Turkey
الوقت: الأحد ١٦-٤-٢٠١٧
الثمن: ٣٠ ليرة"""

JOB_DETAILS = """التفاصيل:
إصلاح مغسلة ماء ليست تعمل جيدا، لا يخرج منها ماء أبدا ويصعب تحريك مقبضها."""

JOB_CONFIRMATION = "السيد محمد في انتظارك!"
CUSTOMER_CONFIRM = "job confirm"
client = Client(ACCOUNT_SID, AUTH_TOKEN)

STATE = "PROPOSING"

@app.route("/")
def hello():
  return "Bla Bla"

@app.route("/send")
def send_sms():
  global client
  print 'Sending a message...'
  new_message = client.messages.create(to=PHONE, from_='+19143025185', body=JOB_REQUEST)
  return "Thank you!"

@app.route("/receive_sms")
def receive_sms():
  global STATE

  if STATE == "PROPOSING":
    new_message = client.messages.create(to=PHONE, from_='+19143025185', body=JOB_DETAILS)
    STATE = "DETAILS"
  elif STATE == "DETAILS":
    new_message_1 = client.messages.create(to=PHONE, from_='+19143025185', body=JOB_CONFIRMATION)
    new_message_2 = client.messages.create(to=CUSTOMER, from_='+19143025185', body=CUSTOMER_CONFIRM)
    STATE = "OK"
  else:
    new_message_1 = client.messages.create(to=PHONE, from_='+19143025185', body='OK')
    new_message_2 = client.messages.create(to=CUSTOMER, from_='+19143025185', body='Job Done. 50USD debited from your credit card.')
    STATE = "PROPOSING"

  return "OK!"

  

if __name__ == "__main__":
  app.run()
