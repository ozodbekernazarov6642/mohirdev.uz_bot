from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import Message
from keyboards.default.KursBackendKeyboard import menuBackendKeyboard
from keyboards.default.KursFrontendKeyboard import menuFrontendKeyboard
from keyboards.default.KursBoshqalarKEyboard import menuBoshqalar
from states.StateStart import StateStart

from loader import dp


@dp.message_handler(Text(equals='Backend'), state=StateStart.Kurs)
async def backendKurs(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuBackendKeyboard)



@dp.message_handler(Text(equals='Frontend'), state=StateStart.Kurs)
async def frontendKurs(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuFrontendKeyboard)


@dp.message_handler(Text(equals='Boshqalar'), state=StateStart.Kurs)
async def boshqaKurs(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuBoshqalar)



