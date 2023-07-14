from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuKasbKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Mobil Dasturlash"),
            KeyboardButton(text="Backend")
        ],
        [
            KeyboardButton(text="Full Stack"),
            KeyboardButton(text="Sun'iy intellekt")
        ],
        [
            KeyboardButton(text="Frontend"),
            KeyboardButton(text="Dizayn")
        ],
        [

            KeyboardButton(text="Boshqalar")
        ]
    ],
    resize_keyboard=True,
    row_width=2
)