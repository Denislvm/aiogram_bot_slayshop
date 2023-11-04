from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# 'start', 'help'
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вітаю тебе, у моему магазині!🙌👠🥵', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/kost_costBot")


#'Как_связаться?'
async def contact_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Для уточнення інформації або замовлення ви можете зв'язатись зі мною у instagram, telegram.\n"
                                                 "instagram - https://www.instagram.com/slayshop.kk/; \n "
                                                 "telegram profile - @lightingmcqueenhoe.\n")
    


async def about_market_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Slay Shop | ua🤍\n"
                                                 "✨рада вітати тебе тут✨"
                                                 "\n⚡️відправка нп і уп 3-4 рази на тиждень"
                                                 "\n⚡️працюємо по повній передплаті або пп 150 гривень🙌🏼")


async def catalog_clothing_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(contact_command, commands=['Як_звязатись'])
    dp.register_message_handler(about_market_command, commands=['О_магазині'])
    dp.register_message_handler(catalog_clothing_command, commands=['Каталог_товарів'])
