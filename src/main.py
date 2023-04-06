from aiogram import Bot, Dispatcher, executor, types
from utils.config_handler import ConfigHandler
from handlers.handler import BotHandler

ch = ConfigHandler('/Users/vsevolodpopov/Dev/Chat_bot/v3/config.yaml')
config = ch.load_config()

bot = Bot(token=config['API_TOKEN'])
dp = Dispatcher(bot)

bot_handler = BotHandler(dp)
bot_handler.add_handlers()

 

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)