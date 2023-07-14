from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuBackendKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="PHP & Yii Dasturlash"),
        ],
        [
            KeyboardButton(text="Node.JS praktikum"),
            KeyboardButton(text=".NET Dasturlash")
        ]
    ],
    resize_keyboard=True
)