from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import ContentType, Message

TOKEN: str = '5749798856:AAHZOqFyeaKVZB5_Nby0zDI3HP7-UhFAYlU'

bot: Bot = Bot(TOKEN)
dp: Dispatcher = Dispatcher()


async def on_startup(_):
    print('бот работает')


async def start_command(message: Message):
    await message.answer('Привет!')


async def help_command(message: Message):
    await message.answer('Напиши что нибудь')


async def send_foto(message: Message):
    await message.reply_photo(message.photo[0].file_id)


async def send_echo(message: Message):
    await message.reply(text=message.text)


async def sticer_echo(message: Message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHlfdj3n6cwKQRAAF9pbSI8whALaymfEQAAngLAALhKfhJwpGRNpsVMCUuBA')


dp.message.register(start_command, Command(commands=['start']))
dp.message.register(help_command, Command(commands=['help']))
dp.message.register(send_foto, F.photo)
dp.message.register(send_echo)
dp.message.register(sticer_echo, Command(commands=['sticer']))


if __name__ == '__main__':
    dp.run_polling(bot,
                   on_startup=on_startup)
