from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(text='Front-End Dasturlash',state=StateStart.Kasb)
async def FrontEndKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Front-End Dasturlash\n"
               "\n"
               "Kurs muallifi: Muhammadjavohir Sur'atov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/628f1f83ec711dcc47d151c8/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()