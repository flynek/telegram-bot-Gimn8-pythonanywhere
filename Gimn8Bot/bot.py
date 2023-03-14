from aiogram.utils import executor
from create_bot import dp
from handlers import clients

clients.register_handlers_clients(dp)


async def on_startup(_):
    print('Бот в онлайне!')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
# ставим условие, что бот получает сообщения только пока онлайн
