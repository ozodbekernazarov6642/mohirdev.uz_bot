from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(text="Git boshqaruv tizimi",state=StateStart.Kurs)
async def GitKurs(msg: Message, state:FSMContext):
    message = ("Kurs nomi: Git boshqaruv tizimi\n"
               "\n"
               "Kurs muallifi: Farhod Dadajonov\n"
               "\n"
               "Kurs narxi: Bepul \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264b669d972027cd02e9a")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text="TS asoslari",state=StateStart.Kurs)
async def TSKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: TypeScript asoslari\n"
               "\n"
               "Kurs muallifi: Farhod Dadajonov\n"
               "\n"
               "Kurs narxi: Bepul \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264c069d972027cd031e9/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()



@dp.message_handler(text="Kotlinda algoritim va masalalar",state=StateStart.Kurs)
async def KotlinKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Kotlinda algoritim va masalalar\n"
               "\n"
               "Kurs muallifi: Zohidjon Akbarov\n"
               "\n"
               "Kurs narxi: Bepul \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264c569d972027cd03355/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()