from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from Handlers.table_Menu import readTable, getFood


async def show_food(message: types.Message):
    await message.reply(readTable())


async def get_type_of_food(message: types.Message):
    await message.reply(getFood(message.text))


def register_handler(dp: Dispatcher):
    dp.register_message_handler(show_food, Text(equals="Меню", ignore_case=True))
    dp.register_message_handler(get_type_of_food, Text(equals='Пицца' or 'Хот дог' or 'Шаурма', ignore_case=True))
