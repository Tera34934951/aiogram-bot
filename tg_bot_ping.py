import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message

API_TOKEN = '6091713346:AAGRQQbyvweSBpL01cNXhd3uHQB6vAosI_E' # токен
ADMIN = 5943169969 #id admin

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class dialog(StatesGroup):
    spam = State()
    blacklist = State()
    whitelist = State()
    command = State()
    all_command = State()

#Добавить расписание

@dp.message_handler(content_types=['text'], text='пр')
async def add_command(message: Message):
    if message.from_user.id == ADMIN:
        await message.answer('''Привет я начинающий конструктор меня создали для развития и изучения библиотеки aiogram для телеграма.''')
        await dialog.command.set()
    else:
        await message.answer('Вы не являетесь админом')






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)