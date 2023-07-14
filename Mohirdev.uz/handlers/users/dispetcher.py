from aiogram import types
from states.StateStart import StateStart
from loader import dp



@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Menyulardan birini tanlang")

@dp.message_handler(state=StateStart.Kasb)
@dp.message_handler(state=StateStart.Kurs)
async def bot_echo(message: types.Message):
    await message.answer("Menyulardan birini tanlang")
