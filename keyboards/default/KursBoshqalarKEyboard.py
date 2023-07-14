from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuBoshqalar = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Git boshqaruv tizimi"),
            KeyboardButton(text="TS asoslari")
        ],
        [
            KeyboardButton(text="Kotlinda algoritim va masalalar")
        ]
    ],
    resize_keyboard=True
)