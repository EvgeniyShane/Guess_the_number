import json
import logging
from dotenv import load_dotenv
import os
import controllers.start as start
from pymongo import MongoClient
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not API_TOKEN:
    raise ValueError("No API token provided")
else:
    print("Api token is successfully loaded")

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_database():
    MONGO_URL = os.getenv("MONGO_DB_URL")
    client = MongoClient(MONGO_URL)
    return client['test']

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')
greet_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    ).row(button1, button2, button3)

@dp.message_handler(commands=['some'])
async def some(message: Message):
    database = get_database()
    # find first document in collection and exclude _id field
    data = database.test.find_one({}, {'_id': False})
    print(data)
    await bot.send_message(487541823, json.dumps(data))

@dp.message_handler(commands=['first'])
async def first(message: Message):
    m = """
    *What is the capital of the United States of America?*
    [New York](https://en.wikipedia.org/wiki/New_York_City)
    """
    await bot.send_message(487541823, parse_mode="Markdown", text=m)

@dp.message_handler(commands=['second'])
async def process_start_command(message: Message):
    await message.reply("Привет!", reply_markup=greet_kb)


if __name__ == '__main__':
    start.setup(dp)
    executor.start_polling(dp, skip_updates=True)