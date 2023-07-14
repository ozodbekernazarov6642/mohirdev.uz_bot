from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(text='Social Media Design',state=StateStart.Kasb)
async def SMDKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Social Media Design\n"
               "\n"
               "Kurs muallifi: Ismoil Safarov\n"
               "\n"
               "Kurs narxi: 1.000.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62b057b600adbba3a3921843/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text='UX/UI Design',state=StateStart.Kasb)
async def U_U_Dasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: UX/UI Design\n"
               "\n"
               "Kurs muallifi: Ismoil Safarov\n"
               "\n"
               "Kurs narxi: 1.800.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62b05838c562ef3caff78e2f/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()