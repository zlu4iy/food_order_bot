from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import (get_categories, get_soups, get_second_dishes, get_salades, get_garnirs,
                                   get_independent_dish)
from logger import logging as log

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Первое'), KeyboardButton(text='Второе')],
                                     [KeyboardButton(text='Гарнир'), KeyboardButton(text='Салаты')],
                                     [KeyboardButton(text='Самостоятельное блюдо')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...'
                           )
# get_name = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить Имя', request_name=True)]],
#                                resize_keyboard=True)


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    # keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def soups(category_id):
    all_soups = await get_soups(category_id)
    keyboard = InlineKeyboardBuilder()
    for dish in all_soups:
        keyboard.add(InlineKeyboardButton(text=dish.name, callback_data=f'dish_{dish.id}'))
    # keyboard.add(InlineKeyboardButton(text='В начало', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def second_course(category_id):
    all_second_dishes = await get_second_dishes(category_id)
    keyboard = InlineKeyboardBuilder()
    for dish in all_second_dishes:
        keyboard.add(InlineKeyboardButton(text=dish.name, callback_data=f'dish_{dish.id}'))
    # keyboard.add(InlineKeyboardButton(text='В начало', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def salades(category_id):
    all_salades = await get_salades(category_id)
    keyboard = InlineKeyboardBuilder()
    for dish in all_salades:
        keyboard.add(InlineKeyboardButton(text=dish.name, callback_data=f'dish_{dish.id}'))
    # keyboard.add(InlineKeyboardButton(text='В начало', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def garnirs(category_id):
    all_garnirs = await get_garnirs(category_id)
    keyboard = InlineKeyboardBuilder()
    for dish in all_garnirs:
        keyboard.add(InlineKeyboardButton(text=dish.name, callback_data=f'dish_{dish.id}'))
    # keyboard.add(InlineKeyboardButton(text='В начало', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def independent_dish(category_id):
    all_independent_dishes = await get_independent_dish(category_id)
    keyboard = InlineKeyboardBuilder()
    for dish in all_independent_dishes:
        keyboard.add(InlineKeyboardButton(text=dish.name, callback_data=f'dish_{dish.id}'))
    # keyboard.add(InlineKeyboardButton(text='В начало', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()



