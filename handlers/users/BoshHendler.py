from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from keyboards.default.KasbKeyboard import menuKasbKeyboard
from keyboards.default.KursKeyboard import menuKursKeyboard
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(Text(equals='Kasb'))
async def kesb(msg: types.Message):
    await msg.answer("Kategoriya tanlang", reply_markup=menuKasbKeyboard)
    await StateStart.Kasb.set()

@dp.message_handler(Text(equals="Kurs"))
async def kurs(msg: types.Message):
    await msg.answer("Kategoriya tanlang", reply_markup=menuKursKeyboard)
    await StateStart.Kurs.set()