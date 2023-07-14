from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuBoshqalarKeyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="QA - тестировщик"),
            KeyboardButton(text="English for IT")
        ],
        [
            KeyboardButton(text="Robototexnika"),
            KeyboardButton(text="Project Management")
        ],
        [
            KeyboardButton(text="Digital Marketing & Ecommerce")
        ]
    ],
    resize_keyboard=True
)