from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))  # получаем токен бота
dp = Dispatcher(bot)  # вторым параметром указывам хранилище
