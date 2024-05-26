from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq


router = Router()

class Register(StatesGroup):
    name = State()
    sirname = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Привет! Я обЖора_бот!', reply_markup=kb.main)    # Прикрепляем клавиатуру в ответ на старт бота.


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите Ваше имя.')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.sirname)
    await message.answer('Введите Вашу фамилию.')

@router.message(Register.sirname)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(sirname=message.text)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаша фамилия: {data["sirname"]}')
    await state.clear()
#
#
# @router.message(F.text == 'Первое')
# async def cmd_soup(message: Message):
#     await message.answer('Выберите супчик.', reply_markup=kb.first_course)

@router.message(F.text == 'Первое')
async def catalog(message: Message):
    await message.answer('Выберите супчик.', reply_markup=await kb.soups(1))

@router.message(F.text == 'Второе')
async def catalog(message: Message):
    await message.answer('Что на горячее?', reply_markup=await kb.second_course(2))

@router.message(F.text == 'Гарнир')
async def catalog(message: Message):
    await message.answer('Выберите гарнир?', reply_markup=await kb.garnirs(3))

@router.message(F.text == 'Салаты')
async def catalog(message: Message):
    await message.answer('Выберите салат?', reply_markup=await kb.salades(4))

@router.message(F.text == 'Самостоятельное блюдо')
async def catalog(message: Message):
    await message.answer('Выберите блюдо', reply_markup=await kb.independent_dish(5))

# @router.callback_query(F.data.startswith('category_'))
# async def category(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию')
#     await callback.message.answer('Выберите блюдо', reply_markup=await kb.soups(callback.data.split('_')[1]))
