from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menuBackendKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Mukammal Telegram Bot"),
        ],
        [
            KeyboardButton(text='C++ Asoslari'),
            KeyboardButton(text="Python Asoslari")
        ],
        [
            KeyboardButton(text="Professional Node.JS"),
            KeyboardButton(text="Django3: Python Full stack")
        ],
        [

            KeyboardButton(text="Python: Ma'lumotlar tuzilmasi")
        ],
        [
            KeyboardButton(text="PostgreSQL"),
            KeyboardButton(text="Yii2 Framework")
        ],
        [
            KeyboardButton(text="Django Rest Framework")
        ]
    ],
    resize_keyboard=True
)