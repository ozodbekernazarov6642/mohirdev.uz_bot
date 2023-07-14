from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.StateStart import StateStart
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=StateStart.Kurs)
async def bot_help(message: types.Message, state:FSMContext):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
    await state.finish()

@dp.message_handler(CommandHelp(), state=StateStart.Kasb)
async def bot_help(message: types.Message, state:FSMContext):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
    await state.finish()

