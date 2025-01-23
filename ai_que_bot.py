from telebot import TeleBot 
class Bot:
    def __init__(self):
        self.bot = TeleBot('7775550429:AAFxKOxWht_KslpQjPI16Dq28ppFOgRtUQo', skip_pending = True)
        self.decorators()        
        while True:
            if __name__ == '__main__':
                try:
                    self.bot.polling(none_stop = True, interval = 0)
                except:
                    pass
    def decorators(self):
        @self.bot.message_handler(commands = ['start'])
        def start(message):
            answer_start = f'''Привет, {message.from_user.first_name} {message.from_user.last_name}!
                Задай мне интересующий тебя вопрос в максимально понятной и простой форме, соблюдая грамматические и орфографические нормы
            '''.replace(' !', '!').replace('    ', '')
            self.bot.send_message(message.from_user.id, answer_start)
        @self.bot.message_handler(content_types = ['text'])
        def text(message):
            if message.from_user.id != 5098568058:
                self.bot.send_message(message.text.split(' * ')[0], message.text.split('*')[1])            
            else:
                self.bot.send_message('5098568058', f'{message.from_user.id} * {message.text}')
bot_instance = Bot()
