from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import ContentType, Message

TOKEN: str = '5749798856:AAHZOqFyeaKVZB5_Nby0zDI3HP7-UhFAYlU'

bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('привет')

@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('напиши что нибудь')

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='нет данного типа апдейта')

if __name__ == '__main__':
    dp.run_polling(bot)
