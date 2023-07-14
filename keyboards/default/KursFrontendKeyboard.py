from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuFrontendKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="HTMLda dasturlash"),
            KeyboardButton(text="Frontend asoslari")
        ]
    ],
    resize_keyboard=True
)