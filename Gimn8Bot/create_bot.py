from aiogram import Bot
from aiogram.dispatcher import Dispatcher

proxy_url = 'http://proxy.server:3128'
TOKEN = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)
