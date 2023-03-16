from aiogram.utils import executor
from create_bot import dp
from handlers import clients
import logging

clients.register_handlers_clients(dp)
logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('Бот в онлайне!')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

