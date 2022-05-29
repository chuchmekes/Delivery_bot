from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu_button = KeyboardButton("Меню")
order_button = KeyboardButton("Сделать заказ")
review_button = KeyboardButton("Оставить отзыв")
telephone_button = KeyboardButton("Телефоны для справки")

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(menu_button, order_button).row(review_button, telephone_button)

cancel_button = KeyboardButton("Отменить заказ")

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(cancel_button)

cancel_button_two = KeyboardButton('Отменить отзыв')

kb_cancel_two = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel_two.add(cancel_button_two)