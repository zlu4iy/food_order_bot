from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Первое'), KeyboardButton(text='Второе')],
                                     [KeyboardButton(text='Гарнир'), KeyboardButton(text='Салаты')],
                                     [KeyboardButton(text='Самостоятельное блюдо')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...'
                           )

first_course = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Суп "Борщ"', callback_data='borsch_soup')],
    [InlineKeyboardButton(text='Суп "Куриный с фрикадельками"', callback_data='chicken_ball_soup')],
    [InlineKeyboardButton(text='Суп "Грибной"', callback_data='mashroom_soup')],
    [InlineKeyboardButton(text='БЕЗ СУПА', callback_data='no_soup')]
]
)
