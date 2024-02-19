import logging
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import os
#1 Функция для перевода

def transliterate(text):
    # Создаем словарь для соответствия кириллических символов и их транслитерации
    translit_table = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
        'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ы': 'y', 'ъ': 'ie', 'э': 'e', 'ю': 'iu', 'я': 'ia'
    }

    # Транслитерируем текст
    transliterated_text = ''
    for char in text:
        transliterated_text += translit_table.get(char, char)

    return transliterated_text

#2 Инициализация объектов

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

#3 Обработка команды /start

@dp.message(Command(commands=['start']))
async def process_command_start(message:Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет {user_name}, отправь свое ФИО и мы отправим твоё ФИО латинскими буквами!'
    logging.info(f'{user_name} {user_id} Запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

#4 Обработка всех сообщений

@dp.message()
async def cyrrylic_to_larinic(message:Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    fio_cyrillic = message.text
    fio_latin = transliterate(fio_cyrillic).title()
    logging.info(f'{user_name} {user_id} {fio_cyrillic} to {fio_latin}')
    await message.answer(text=fio_latin)

#5 Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)
