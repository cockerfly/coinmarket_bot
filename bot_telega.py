from aiogram import Bot, Dispatcher, executor, types
import os
import asyncio
from aiogram.types import ChatActions
from parser import collect_data
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json
import  time
#from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='Your_TOKEN', parse_mode=types.ParseMode.HTML)

dp =Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_buttons = types.KeyboardButton("Курсы валют 💵")
    free_btc = types.KeyboardButton("Free bitcoin")
    #keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #keyboard.add(*start_buttons)
    keyboard.add(start_buttons, free_btc)

    await message.answer("🔥Самые актуальные курсы криптовалют🔥", reply_markup=keyboard)

url_free = InlineKeyboardMarkup(row_width=2)
url_button1 = InlineKeyboardButton(text="Free btc_1", url="https://bit.ly/3EkJJjT")
url_button2 = InlineKeyboardButton(text="Free btc_2", url="https://bit.ly/3CflTDs")

url_free.add(url_button1, url_button2)
@dp.message_handler(Text(equals="Free bitcoin"))
async def free_btc(message=types.Message):
    await message.answer("BTC fo free", reply_markup=url_free)


@dp.message_handler(Text(equals="Курсы валют 💵"))
async def get_discount_sneakers(message: types.Message):
    await message.answer("Ожидайте...")

    collect_data()
    with open('result_data.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hbold("Валюта: ")} {item.get("Name")}\n' \
            f'{hbold("Цена: ")} {item.get("price")}💲\n' \

        if index%20 == 0:
            time.sleep(4)
        if index >=99:
            end = f'{hbold("На этом пока все 😊 ")}\n'
            return await message.answer(end)
        print(index)

        await message.answer(card)
        
def main():
    executor.start_polling(dp, skip_updates=True)



if __name__== "__main__":
    main()