from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuKursKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Backend"),
            KeyboardButton(text="Frontend")
        ],
        [
            KeyboardButton(text="Boshqalar")
        ]
    ],
    resize_keyboard=True,
)