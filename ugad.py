import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import  Text, Command

BOT_TOKEN: str = '5749798856:AAHZOqFyeaKVZB5_Nby0zDI3HP7-UhFAYlU'

bot: Bot =  Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 10

user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}

def get_random_number() -> int:
    return random.randint(1, 100)

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила и список доступных'
                         'команд - отправь команду /help')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\nЯ загадываю число от 1 до 100, у тебя есть {ATTEMPTS} '
                         f'попыток что бы угадать его' )

@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]})\n'
                         f'игр выиграно: {user["wins"]}')

@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Захотите играть'
                             'напишите об этом')
        user['in_game'] = False
    else:
        await message.answer('А мы не играем, может сыграем?')

@dp.message(Text(text=['Да','Давай','Сыграем','Игра','Играть','Хочу играть'], ignore_case=Text))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer('Ура, я загадал число от 1 до 100')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем я могу реагировать на/n'
                             'число от 1 до 100 и команды /cansel /start')

@dp.message(Text(text=['Нет','Не хочу','Не буду'], ignore_case=Text))
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer('Жало, если захочешь играть просто напиши об этом')
    else:
        await message.answer('Мы же сейчас играем'
                             'присылайте число от 1 до 100')

@dp.message(lambda x: x.text and x.text.isdigit() and  1 <= int(x.text) <= 100)
async def procces_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Вы угадали число!'
                                 'Сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Мое чило меньше')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Мое чило больше')
            user['attempts'] -= 1
        if user['attempts'] == 0:
            await message.answer(f'Вы проиграли, мое число было {user["secret_number"]}')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await  message.answer('Мы еще не играем, хотите сыграть?')

@dp.message()
async def process_other_text_answer(message: Message):
    if user['in_game']:
        await message.answer('Мы с вами играем'
                             'Пришлите число от 1 до 100')
    else:
        await message.answer('Я довольно ограниченый бот'
                             'давай просто сыграем')






if __name__ == '__main__':
    dp.run_polling(bot)



