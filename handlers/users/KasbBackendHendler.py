from aiogram.types import Message, ReplyKeyboardRemove
from states.StateStart import StateStart
from aiogram.dispatcher import FSMContext

from loader import dp

@dp.message_handler(text="PHP & Yii Dasturlash",state=StateStart.Kasb)
async def PHP_YiiKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: PHP & Yii Dasturlash\n"
               "\n"
               "Kurs muallifi: Sardor Dushamov\n"
               "\n"
               "Kurs narxi: 2.000.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/63f4a3a973dc4b8d7a8e5722/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text="Node.JS praktikum",state=StateStart.Kasb)
async def NodeJsKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Node.JS praktikum\n"
               "\n"
               "Kurs muallifi: Bexruz Xolmuminov\n"
               "\n"
               "Kurs narxi: 1.600.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/63f0b69273dc4b8d7a88710c/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text=".NET Dasturlash",state=StateStart.Kasb)
async def NetKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: .NET Dasturlash\n"
               "\n"
               "Kurs muallifi: Elbek Normurodov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62d42f08bbec522944709808/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()