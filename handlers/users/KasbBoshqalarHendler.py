from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.StateStart import StateStart

from loader import dp

@dp.message_handler(text='QA - тестировщик',state=StateStart.Kasb)
async def QA_T_Kasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: QA - тестировщик\n"
               "\n"
               "Kurs muallifi: Muhammadaziz Xoliqberdiyev\n"
               "\n"
               "Kurs muallifi: Abdufattoh Abdurahmonov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62d9306a8265902157887f0f/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()



@dp.message_handler(text='English for IT',state=StateStart.Kasb)
async def EngITKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: English for IT\n"
               "\n"
               "Kurs muallifi: Behzod Botirov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/627538a27072fde45728064c/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text='Robototexnika',state=StateStart.Kasb)
async def RobotoKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Robototexnika\n"
               "\n"
               "Kurs muallifi: Azizbek Xolmonov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/63ef58777d77adfbd149555e/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text='Project Management',state=StateStart.Kasb)
async def PMKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Project Management\n"
               "\n"
               "Kurs muallifi: Abdulla Xaydarov\n"
               "\n"
               "Kurs narxi: 2.000.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/632a935120b1d593f0b3f9d5/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text='Digital Marketing & Ecommerce',state=StateStart.Kasb)
async def DMEKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Front-End Dasturlash\n"
               "\n"
               "Kurs muallifi: Muhammad Xalil\n"
               "\n"
               "Kurs muallifi: Muslim Rahmonov\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62975625f65a209b79472277/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()