from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import database
import ui
from bot import bot, dp, logger


# Хэндлер запуска
@dp.message_handler(commands='tasks')
@dp.message_handler(Text(equals=ui.BUT_TASKS))
async def show_tasks(message: types.Message, state: FSMContext):
    await state.finish()

    tasks = database.get_tasks()
    tasks_keyboard = types.InlineKeyboardMarkup(row_width=1)

    for task in tasks:
        task_but = types.InlineKeyboardButton(task['name'], callback_data=f"task={task['id']}")
        tasks_keyboard.add(task_but)

    await message.answer(ui.TEXT_TASKS, reply_markup=tasks_keyboard)


@dp.callback_query_handler(Text(startswith='task='), state='*')
async def show_task(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    id = int(callback.data.split('=')[1])

    task = database.get_task(id)

    text = task['name'] + '\n----------------\n' + task['desc']
    file_path = task['file_path']
    image_path = task['image_path']

    keyboard = types.InlineKeyboardMarkup(row_width=1)
   
    keyboard.add(types.InlineKeyboardButton(ui.TEXT_TASK_FILE, callback_data=f"taskfile={file_path}"))
    keyboard.add(types.InlineKeyboardButton(ui.TEXT_TASK_TOPICS, callback_data=f"tasktopics={id}"))
    keyboard.add(types.InlineKeyboardButton(ui.TEXT_TASK_HELP, callback_data=f"help={id}"))

    await callback.answer()

    if image_path: 
        await bot.send_photo(callback.from_user.id, types.InputFile(image_path), caption=text, parse_mode='HTML', reply_markup=keyboard)
    else:
        await bot.send_message(callback.from_user.id, text, parse_mode='HTML', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='help='), state='*')
async def show_task_help(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    id = int(callback.data.split('=')[1])

    task = database.get_task(id)

    await bot.send_message(callback.from_user.id, task['help_text'], parse_mode='HTML')


@dp.callback_query_handler(Text(startswith='taskfile='), state='*')
async def show_task_file(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    file_path = str(callback.data.split('=')[1])

    await callback.answer()
    await bot.send_document(callback.from_user.id, types.InputFile(file_path), caption=ui.TEXT_TASK_FILE, parse_mode='HTML')


@dp.callback_query_handler(Text(startswith='tasktopics='), state='*')
async def show_task_topics(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()

    id = int(callback.data.split('=')[1])

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    topics = database.get_task_topics(id)
    for topic in topics:
            keyboard.add(types.InlineKeyboardButton(topic['name'], callback_data=f"topic={topic['id']}"))

    await callback.answer()
    await bot.send_message(callback.from_user.id, ui.TEXT_TASK_TOPICS, reply_markup=keyboard, parse_mode='HTML')