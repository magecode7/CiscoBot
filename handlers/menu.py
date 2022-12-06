from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import database
import ui
from bot import dp, logger


# Хэндлер запуска
@dp.message_handler(commands='start', state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await dp.bot.set_my_commands(ui.commands)  # Установка комманд

    await message.answer_photo(types.InputFile('images/cisco.jpg') ,caption=ui.TEXT_MENU_START, reply_markup=ui.keyboard_main)


# Возвращение назад
@dp.message_handler(commands='back', state='*')
@dp.message_handler(Text(equals=ui.BUT_BACK), state='*')
async def back_to_menu(message: types.Message, state: FSMContext):
    await state.finish()

    await message.answer(ui.TEXT_BACK, reply_markup=ui.keyboard_main)


# Возвращение назад
@dp.message_handler(commands='faq', state='*')
@dp.message_handler(Text(equals=ui.BUT_FAQ), state='*')
async def show_faq(message: types.Message, state: FSMContext):
    await state.finish()

    await message.answer(ui.TEXT_FAQ, reply_markup=ui.keyboard_main)