from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuMobilKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Android & Kotlin Dasturlash"),
            KeyboardButton(text="IOS & Swift Dasturlash")
        ]
    ],
    resize_keyboard=True,
    row_width=1
)