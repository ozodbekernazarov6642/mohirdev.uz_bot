from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuStartKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Kasb"),
            KeyboardButton(text="Kurs")
        ]
    ],
    resize_keyboard=True
)