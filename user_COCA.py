from pyrogram import Client 
from time import sleep

bot = Client(name = 'hwgooood', api_id = '27540501', api_hash = '88ddbe990b3c5f383c35f42bb87e7f8a', phone_number = '+79957835128')

strings = ['окак', 'пупупу', 'вот такие пироги', 'мда', 'эх', 'ого', 'жесть', 'мдааа', 'пп']

bot.start()

for i in strings:
    bot.send_message(chat_id = -1001627708951, text = i)
    sleep(200)

bot.stop()
