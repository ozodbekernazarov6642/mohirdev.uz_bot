from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import Text
from states.StateStart import StateStart
from keyboards.default.KasbMobilKeyboard import menuMobilKeyboard
from keyboards.default.KasbBackendKeyboard import menuBackendKeyboard
from keyboards.default.KasbFullstackKeyboard import menuFullstackKeyboard
from keyboards.default.KasbSuniyintellektKeyboard import menuSuniyintellektKeyboard
from keyboards.default.KasbFrontendKeyboard import menuFrontendKeyboard
from keyboards.default.KasbDizaynKeyboard import menuDizaynKeyboard
from keyboards.default.KasbBoshqakarKEyboard import menuBoshqalarKeyboard

from loader import dp


@dp.message_handler(Text(equals="Mobil Dasturlash"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuMobilKeyboard)


@dp.message_handler(Text(equals="Backend"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuBackendKeyboard)


@dp.message_handler(Text(equals="Full Stack"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuFullstackKeyboard)


@dp.message_handler(Text(equals="Sun'iy intellekt"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuSuniyintellektKeyboard)


@dp.message_handler(Text(equals="Frontend"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuFrontendKeyboard)

@dp.message_handler(Text(equals="Dizayn"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuDizaynKeyboard)


@dp.message_handler(Text(equals="Boshqalar"),state=StateStart.Kasb)
async def MobilKasb(msg: Message):
    await msg.answer("Darsni tanlang", reply_markup=menuBoshqalarKeyboard)
