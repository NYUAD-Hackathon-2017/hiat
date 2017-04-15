#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from flask import Flask

app = Flask(__name__)

ACCOUNT_SID = 'ACcefa2306ccdba981522a00c621e602ab'
AUTH_TOKEN = 'ba3216346af36cf72ad0fb48e45e5b8e'
PHONE = '+971556383129'
CUSTOMER = '+14158573334'

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

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/send")
def send_sms():
  global client
  print 'Sending a message...'
  new_message = client.messages.create(to=PHONE, from_='+19143025185', body=JOB_REQUEST)
  return "Hello World!"

@app.route("/receive_sms")
def receive_sms():
  print 'RECEIVED SMS!'
  return "Received SMS!!!"


if __name__ == "__main__":
  app.run()
