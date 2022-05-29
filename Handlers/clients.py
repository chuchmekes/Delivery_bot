from aiogram import types, Dispatcher
from Keyboards import kb_main, kb_cancel_two
from Handlers.table_Telephones import readTable
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMReview(StatesGroup):
    name = State()
    food = State()
    review = State()


async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте, вас приветствует служба доставки 'Почти вкусная еда'."
                        "Выберите ваше следующее действие.", reply_markup=kb_main)


async def get_telephones(message: types.Message):
    await message.reply(readTable())


async def start_review(message: types.Message):
    await message.reply("Напишите ваше имя", reply_markup=kb_cancel_two)
    await FSMReview.next()


async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Имя'] = message.text
        await FSMReview.next()
        await message.answer("Введите еду для отзыва.")


async def food(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["Еда"] = message.text
        await FSMReview.next()
        await message.answer("Напишите отзыв.")


async def review(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Отзыв'] = message.text
        await message.answer(str(data), reply_markup=kb_main)


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Отзыв отменен.", reply_markup=kb_main)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(get_telephones, Text(equals="Телефоны для справки", ignore_case=True))
    dp.register_message_handler(start_review, Text(equals='Оставить отзыв', ignore_case=True), state=None)
    dp.register_message_handler(cancel, Text(equals="Отменить отзыв", ignore_case=True), state='*')
    dp.register_message_handler(name, state=FSMReview.name)
    dp.register_message_handler(food, state=FSMReview.food)
    dp.register_message_handler(review, state=FSMReview.review)
