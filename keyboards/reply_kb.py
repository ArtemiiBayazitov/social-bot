from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

show_more_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Показать еще')],
    [KeyboardButton(text='Вернуться в начало')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
    )
