from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Як_звязатись')
b2 = KeyboardButton('/О_магазині')
b3 = KeyboardButton('/Каталог_товарів')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).row(b3)
