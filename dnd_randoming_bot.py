from random import *
from telebot import *

bot = TeleBot('7875463499:AAEfcYUvzL86jrhv4CS-GYHA05RTl-7cEuE', skip_pending = True)

@bot.message_handler(content_types = ['text'])

def get_text_message(message):
    dev = ['Frodo_Norkins']
    if message.from_user.username in dev:
        if 'тест' in message.text.lower() or 'test' in message.text.lower():
            bot.send_message(message.chat.id, 'Я работаю!')
        if 'засыпай' in message.text.lower():
            bot.send_message(message.chat.id, 'Бот деактивирован!')
            bot.stop_bot()
    a = message.text.lower().split()
    if len(a) == 6:
        try:
            if a[0] == 'кубик' and a[2] == 'по' and a[3] in ['4', '6', '8', '10', '12', '20'] and a[4] in '+-' and int(a[1]) < 101 and int(a[5]) < 101:
                first_name = ''
                last_name = ''
                st = ''
                sum = 0
                if message.from_user.first_name != None:
                    first_name = message.from_user.first_name
                if message.from_user.last_name != None:
                    last_name = message.from_user.last_name
                for i in range(int(a[1])):
                    rand = randint(1, int(a[3]))
                    if i != int(a[1]) - 1:
                        if a[4] == '-':
                            st += str(rand - int(a[5])) + ', '
                            sum += rand - int(a[5])
                        else:
                            st += str(rand + int(a[5])) + ', '
                            sum += rand + int(a[5])
                    else:
                        if a[4] == '-':
                            st += str(rand - int(a[5]))
                            sum += rand - int(a[5])
                        else:
                            st += str(rand + int(a[5]))
                            sum += rand + int(a[5])
                bot.send_message(message.chat.id, first_name + ' ' + last_name + ', вам выпадает: ' + st + '\nСумма: ' + str(sum))
            elif a[0] == 'кубик':
                bot.send_message(message.chat.id, 'Я вас не понял!')
        except ValueError:
            bot.send_message(message.chat.id, 'Я вас не понял!')
    elif a[0] == 'кубик':   
        bot.send_message(message.chat.id, 'Я вас не понял!')

bot.polling(none_stop = True, interval = 0)
