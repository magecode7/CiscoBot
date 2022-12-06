from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import database
import ui
from fuzzywuzzy import fuzz
from bot import bot, dp, logger, UserStates, config


# Хэндлер запуска
@dp.message_handler(commands='search')
@dp.message_handler(Text(equals=ui.BUT_SEARCH))
async def show_search(message: types.Message, state: FSMContext):
    await UserStates.search.set()

    await message.answer(ui.TEXT_SEARCH, reply_markup=ui.keyboard_back)


@dp.message_handler(state=UserStates.search)
async def handle_search(message: types.Message, state: FSMContext):
    all_texts = database.get_all()
    
    search_keyboard = types.InlineKeyboardMarkup(row_width=1)

    for text in all_texts:
        rate = fuzz.WRatio(message.text, text['text'])
        if rate > config.search_percent:
            task_but = types.InlineKeyboardButton(text['text'], callback_data=text['data'])
            search_keyboard.add(task_but)
    
    if len(search_keyboard.values) > 0: 
        await message.answer(ui.TEXT_SEARCH_RESULTS, reply_markup=search_keyboard)
    else: 
        await message.answer(ui.TEXT_SEARCH_NO_RESULTS)