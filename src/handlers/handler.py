from aiogram import Dispatcher, types

class BotHandler:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher
        
    async def start_handler(self, message: types.Message):
        # обработчик команды /start
        await message.reply("Привет!\nЯ Эхо-бот !\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

        
    async def help_handler(self, message: types.Message):
        # обработчик команды /help
        print(222222)
        pass
        
    async def text_handler(self, message: types.Message):
        # обработчик текстовых сообщений от пользователей
        await message.answer(message.text)
        
    async def photo_handler(self, message: types.Message):
        # обработчик фотографий от пользователей
        print(4444)
        pass
        
    def add_handlers(self):
        # добавление обработчиков в диспетчер
        self.dispatcher.register_message_handler(self.start_handler, commands=['start'])
        self.dispatcher.register_message_handler(self.help_handler, commands=['help'])
        self.dispatcher.register_message_handler(self.text_handler, content_types=types.ContentType.TEXT)
        self.dispatcher.register_message_handler(self.photo_handler, content_types=types.ContentType.PHOTO)

