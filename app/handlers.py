from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет обжора!', reply_markup=kb.main)    # Прикрепляем клавиатуру в ответ на старт бота.


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нужна помощь? Неужто отравился?')


@router.message(F.text == 'Первое')
async def cmd_soup(message: Message):
    await message.answer('Выберите супчик.', reply_markup=kb.first_course)
