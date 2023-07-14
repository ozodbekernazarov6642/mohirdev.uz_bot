from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(text="Sun'iy intellekt - NLP", state=StateStart.Kasb)
async def SI_Kasb(msg:Message, state:FSMContext):
    message = ("Kurs nomi: Sun'iy intellekt - NLP\n"
               "\n"
               "Kurs muallifi: Adham Zohirov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/64099e36a70362d863f68f1c/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(text="Data Science va Sun'iy intellekt", state=StateStart.Kasb)
async def DC_SI_Kasb(msg:Message, state:FSMContext):
    message = ("Kurs nomi: Data Science va Sun'iy intellekt\n"
               "\n"
               "Kurs muallifi: Anvar Narzullayev\n"
               "\n"
               "Kurs muallifi: Mansurbek Abdullayev\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62753e60919a3a1c62541aec/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()
