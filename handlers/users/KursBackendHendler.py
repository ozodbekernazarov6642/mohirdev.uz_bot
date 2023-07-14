from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart

from loader import dp



@dp.message_handler(Text(equals="Mukammal Telegram Bot"),state=StateStart.Kurs)
async def MTBKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Mukammal Telegram Bot\n"
               "\n" 
              "Kurs muallifi: Anvar Narzullayev\n"
               "\n" 
              "Kurs narxi: 247.000 so'm\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264c869d972027cd033c3")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()



@dp.message_handler(Text(equals="C++ Asoslari"),state=StateStart.Kurs)
async def CppKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: C++ Asoslari\n"
               "\n" 
              "Kurs muallifi: Qudrat Abduraximov\n"
               "\n" 
              "Kurs narxi: 1.000.000 so'm\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264a369d972027cd02963/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals="Python Asoslari"),state=StateStart.Kurs)
async def PythonKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Python Asoslari\n"
               "\n" 
              "Kurs muallifi: Anvar Narzullayev\n"
               "\n" 
              "Kurs narxi: Bepul\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264af69d972027cd02d52/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals="Professional Node.JS"),state=StateStart.Kurs)
async def NodeJsKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Professional Node.JS\n"
               "\n" 
              "Kurs muallifi: Behruz Xolmominov\n"
               "\n" 
              "Kurs narxi: 247.000 so'm\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264bd69d972027cd030f4/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals="Django3: Python Full stack"),state=StateStart.Kurs)
async def DjangoFsKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Django3: Python Full stack\n"
               "\n" 
              "Kurs muallifi: Anvar Narzullayev\n"
               "\n" 
              "Kurs narxi: Bepul\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264bf69d972027cd03180/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals="Python: Ma'lumotlar tuzilmasi"),state=StateStart.Kurs)
async def PythonMtKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Python: Ma'lumotlar tuzilmasi\n"
               "\n" 
              "Kurs muallifi: Anvar Narzullayev\n"
               "\n" 
              "Kurs narxi: Bepul\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264b769d972027cd02ea8/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(Text(equals="PostgreSQL"),state=StateStart.Kurs)
async def PSQLKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: PostgreSQL\n"
               "\n" 
              "Kurs muallifi: Behruz Xolmominov\n"
               "\n" 
              "Kurs narxi: Bepul\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264ad69d972027cd02d02/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals="Yii2 Framework"),state=StateStart.Kurs)
async def Yii2Kurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Yii2 Framework\n"
               "\n" 
              "Kurs muallifi: Sardor Dushamov\n"
               "\n" 
              "Kurs narxi: Bepul\n"
               "\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/645264ac69d972027cd02cc0/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()



@dp.message_handler(Text(equals="Django Rest Framework"),state=StateStart.Kurs)
async def DjangoKurs(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Django Rest Framework\n" 
              "Kurs muallifi: Muhammad Ertmatov\n" 
              "Kurs narxi: Bepul\n" 
              "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/64526477ecc3657ffcec10e5/free")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()







