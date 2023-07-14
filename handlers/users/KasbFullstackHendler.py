from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(text="Python: Full stack",state=StateStart.Kasb)
async def Python_FsKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Python: Full stack\n"
               "\n"
               "Kurs muallifi: Anvar Narzullayev\n"
               "\n"
               "Kurs muallifi: Jahongir Rahmonov\n"
               "\n"
               "Kurs narxi: 2.000.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/627d0a4e76a27fe16d37634a/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(text="Java: Full stack",state=StateStart.Kasb)
async def Java_FsKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Java: Full stack\n"
               "\n"
               "Kurs muallifi: G'ayratjon Rayimjonov\n"
               "\n"
               "Kurs muallifi: Azizbek Husenov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/6282375876a27fe16d376b49/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()