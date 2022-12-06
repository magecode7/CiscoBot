import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import config
import ui

# Логирование
logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG)
logger_handler = logging.FileHandler('bot.log')
logger_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)
# Хранилище состояний
storage = MemoryStorage()
# Бот токен
bot = Bot(token=config.token)
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)


class UserStates(StatesGroup):
    search = State()


# При включении
async def on_startup(dp):
    logger.debug('Bot started!')

    await bot.send_message(config.admin, ui.TEXT_BOT_STARTUP)


# При отключении
async def on_shutdown(dp):
    logger.debug('Bot shutdown!')

    await bot.send_message(config.admin, ui.TEXT_BOT_SHUTDOWN)


def start_bot():  # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == "__main__":
    start_bot()
