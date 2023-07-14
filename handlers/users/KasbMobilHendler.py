from aiogram.types import Message, ReplyKeyboardRemove
from states.StateStart import StateStart
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(text="Android & Kotlin Dasturlash",state=StateStart.Kasb)
async def Android_KotlinKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: Android & Kotlin Dasturlash\n"
               "\n"
               "Kurs muallifi: Zohidjon Akbarov\n"
               "\n"
               "Kurs muallifi: Mahmudjon Qalandarov\n"
               "\n"
               "Kurs narxi: 2.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/62976f00aedd38cc9cc63b91/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()



@dp.message_handler(text="IOS & Swift Dasturlash",state=StateStart.Kasb)
async def IOS_SwiftKasb(msg: Message, state: FSMContext):
    message = ("Kurs nomi: IOS & Swift Dasturlash\n"
               "\n"
               "Kurs muallifi: Yunusbek Sadullaev\n"
               "\n"
               "Kurs narxi: 1.500.000 so'm \n"
               "\n"
               "Kurs manzili:https://praktikum.mohirdev.uz/dashboard/practicums/6297655af65a209b794723a5/purchase")
    await msg.answer(message, reply_markup=ReplyKeyboardRemove())
    await state.finish()