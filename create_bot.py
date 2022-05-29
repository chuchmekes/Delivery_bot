from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_Token = '5304201748:AAHd9F8Dxq_4Z8cn0A7Qv5ChIWMLGzuC7dI'


storage = MemoryStorage()

bot = Bot(token=API_Token)
dp = Dispatcher(bot, storage=storage)