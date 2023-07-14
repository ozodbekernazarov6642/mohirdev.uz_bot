from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuFullstackKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Python: Full stack"),
            KeyboardButton(text="Java: Full stack")
        ]
    ],
    resize_keyboard=True
)