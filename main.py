import logging
from aiogram import executor
from create_bot import dp
from Handlers import register_handlers, register_handlers_order, register_handler


logging.basicConfig(level=logging.INFO)

register_handler(dp)
register_handlers_order(dp)
register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)