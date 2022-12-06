from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import database
import ui
from bot import bot, dp, logger


# Хэндлер запуска
@dp.message_handler(commands='topics')
@dp.message_handler(Text(equals=ui.BUT_TOPICS))
async def show_topics(message: types.Message, state: FSMContext):
    await state.finish()

    topics = database.get_topics()
    topics_keyboard = types.InlineKeyboardMarkup(row_width=1)

    for topic in topics:
        topic_but = types.InlineKeyboardButton(topic['name'], callback_data=f"topic={topic['id']}")
        topics_keyboard.add(topic_but)

    await message.answer(ui.TEXT_TOPICS, reply_markup=topics_keyboard)


@dp.callback_query_handler(Text(startswith='topic='), state='*')
async def show_topic(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    id = int(callback.data.split('=')[1])

    topic = database.get_topic(id)

    text = topic['name'] + '\n----------------\n' + topic['desc']
    file_path = topic['file_path']
    image_path = topic['image_path']

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(types.InlineKeyboardButton(ui.TEXT_TOPIC_FILE, callback_data=f"topicfile={file_path}"))
    keyboard.add(types.InlineKeyboardButton(ui.TEXT_TOPIC_TASKS, callback_data=f"topictasks={id}"))

    await callback.answer()
    if image_path: 
        await bot.send_photo(callback.from_user.id, types.InputFile(image_path), caption=text, parse_mode='HTML', reply_markup=keyboard)
    else:
        await bot.send_message(callback.from_user.id, text, parse_mode='HTML', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='topicfile='), state='*')
async def show_topic_file(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    file_path = str(callback.data.split('=')[1])

    await callback.answer()
    await bot.send_document(callback.from_user.id, types.InputFile(file_path), caption=ui.TEXT_TOPIC_FILE, parse_mode='HTML')


@dp.callback_query_handler(Text(startswith='topictasks='), state='*')
async def show_topic_tasks(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    id = int(callback.data.split('=')[1])

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    tasks = database.get_topic_tasks(id)
    for task in tasks:
            keyboard.add(types.InlineKeyboardButton(task['name'], callback_data=f"task={task['id']}"))

    await callback.answer()
    await bot.send_message(callback.from_user.id, ui.TEXT_TOPIC_TASKS, reply_markup=keyboard, parse_mode='HTML')