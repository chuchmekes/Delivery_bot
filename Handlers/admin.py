from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from Keyboards import kb_main, kb_cancel


class FSMAdmin(StatesGroup):
    food = State()
    adress = State()
    Name = State()
    Telephone = State()
    How_to_drive = State()


async def order(message: types.Message):
    await FSMAdmin.food.set()
    await message.reply("Введите название еды.", reply_markup=kb_cancel)


async def insert_food(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Заказ'] = message.text
        await FSMAdmin.next()
        await message.reply('Введите адрес доставки.')


async def insert_adress(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Адрес'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите имя заказчика.")


async def Name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Имя'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите ваш телефон.")


async def insert_telephone(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data["Телефон"] = message.text
        await FSMAdmin.next()
        await message.reply("Каким способом к вам подъезжать?")


async def How_to_drive(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["Способ подъезда"] = message.text
        await message.answer(str(data), reply_markup=kb_main)
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Заказ отменен.", reply_markup=kb_main)


def register_handlers_order(dp: Dispatcher):
    dp.register_message_handler(order, Text(equals='Сделать заказ', ignore_case=True), state=None)
    dp.register_message_handler(cancel, Text(equals='Отменить заказ', ignore_case=True), state="*")
    dp.register_message_handler(insert_food, state=FSMAdmin.food)
    dp.register_message_handler(insert_adress, state=FSMAdmin.adress)
    dp.register_message_handler(Name, state=FSMAdmin.Name)
    dp.register_message_handler(insert_telephone, state=FSMAdmin.Telephone)
    dp.register_message_handler(How_to_drive, state=FSMAdmin.How_to_drive)
