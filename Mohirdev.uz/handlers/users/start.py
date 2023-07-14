from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.StartKeyboard import menuStartKeyboard
from states.StateStart import StateStart
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Bolimni Tanlagn", reply_markup=menuStartKeyboard)

@dp.message_handler(CommandStart(),state=StateStart.Kurs)
async def botKurs_start(message: types.Message, state:FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Bolimni Tanlagn", reply_markup=menuStartKeyboard)
    await state.finish()

@dp.message_handler(CommandStart(),state=StateStart.Kasb)
async def botKurs_start(message: types.Message, state:FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Bolimni Tanlagn", reply_markup=menuStartKeyboard)
    await state.finish()