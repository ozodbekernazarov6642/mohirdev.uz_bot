from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuDizaynKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Social Media Design"),
            KeyboardButton(text="UX/UI Design")
        ]
    ],
    resize_keyboard=True
)