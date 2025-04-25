from telebot import TeleBot
from random import randint

class Tbot:

    owner = [5098568058, '2064027844']

    def __init__(self):
        self.bot = TeleBot('8121220166:AAEfBjF4-KmePAi7ie4exsBI2QAsbGkYlE8', skip_pending = True)
        self.decorators()
        self.bot.polling(none_stop = True, interval = 0)

    def decorators(self):
        @self.bot.message_handler(content_types = ['text'])
        def text(message):
            if message.from_user.id in self.owner:
                if message.text.lower() == 'проверка': self.bot.send_message(message.chat.id, 'К работе готов!')
                elif message.text.lower().split()[0] == 'кубик' and len(message.text.split()) == 6: self.cube_roll(message)
                elif message.text.lower().split()[0] == 'качество' and len(message.text.split()) == 2: self.quality_roll(message)

    def cube_roll(self, message):
        if int(message.text.split()[1]) < 1001 and int(message.text.split()[3]) < 1001:
            answer = f'{message.from_user.first_name} {message.from_user.last_name}, вам выпадает: \n'
            sum_rand = 0
            if message.text.split()[4] in ['+', '-']: 
                for var1 in range(0, int(message.text.split()[1])):
                    current_rand = randint(1, int(message.text.split()[3]))
                    sum_rand += current_rand
                    answer += f'{current_rand}, '
                answer += f'Сумма: {sum_rand + int(message.text.split()[4] + message.text.split()[5])} ({sum_rand} {message.text.split()[4]} {message.text.split()[5]})'
                self.bot.send_message(message.chat.id, answer.replace(', С', '\nС', 2))
            elif message.text.split()[4] in ['++', '--']:
                for var1 in range(0, int(message.text.split()[1])):
                    current_rand = randint(1, int(message.text.split()[3])) + int(message.text.split()[4][0] + message.text.split()[5])
                    sum_rand += current_rand
                    answer += f'{current_rand}, '
                answer += f'Сумма: {sum_rand} ({sum_rand + int(message.text.split()[4][0] + message.text.split()[5]) * int(message.text.split()[1]) * (-1)} {message.text.split()[4]} {message.text.split()[5]}x{message.text.split()[1]})'
                self.bot.send_message(message.chat.id, answer.replace(', С', '\nС', 2))
        else: self.bot.send_message(message.chat.id, 'В вашем запросе присутствуют слишком большие числа!')

instance_Tbot = Tbot() 

while True:
    try:
        if __name__ == '__main__': instance_Tbot = Tbot()            
    except: print(f'Возникла неинициализированая ошибка!')
