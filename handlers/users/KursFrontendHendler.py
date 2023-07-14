from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart
from loader import dp

@dp.message_handler(text="HTMLda dasturlash",state=StateStart.Kurs)
async def HTMLKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: HTMLda dasturlash\n"
               "\n"
               "Kurs muallifi: Ulug'bek Samigjonov\n"
               "\n"
               "Kurs narxi: Bepul\n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264c369d972027cd032a9/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text="Frontend asoslari",state=StateStart.Kurs)
async def FrontendKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Frontend asoslari\n"
               "\n"
               "Kurs muallifi: Muhammadjavohir Sur'atov\n"
               "\n"
               "Kurs narxi: Bepul\n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264ba69d972027cd02fca/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()