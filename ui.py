from aiogram import types

# Кнопки
BUT_TOPICS = '📗 Справочник по темам'
BUT_TASKS = '📕 Банк заданий'
BUT_SEARCH = '🔍 Поиск'
BUT_BACK = '◀ Назад'
BUT_FAQ = '❓ FAQ'
# Тексты
TEXT_BOT_STARTUP = '✅ Бот запущен!'
TEXT_BOT_SHUTDOWN = '❌ Бот отключен!'
TEXT_BACK = '🔙 Возвращение в меню...'
# Меню
TEXT_MENU_START = '🏆 Добро пожаловать! Данный бот предоставляет доступ к обучающему материалу и заданиям курса изучения Cisco и Cisco Packet Tracer.'
# Топики
TEXT_TOPICS = '📗 Темы'
TEXT_TOPIC_FILE = '💾 Прикреплённый учебник'
TEXT_TOPIC_TASKS = '📕 Задания по теме'
# Задания
TEXT_TASKS = '📕 Задания'
TEXT_TASK_FILE = '💾 Прикреплённое задание'
TEXT_TASK_HELP = '❓ Помощь'
TEXT_TASK_TOPICS = '📗 Темы по заданию'
# Поиск
TEXT_SEARCH = '🔍 Введите запрос. Для отмены введите "Назад" или /back:'
TEXT_SEARCH_RESULTS = '🔍 Найденные совпадения:'
TEXT_SEARCH_NO_RESULTS = '❌ Совпадения не найдены!'
# FAQ
TEXT_FAQ = '❗ Данный бот разработан в рамках изучения курса дисциплины \"Системы и сети передачи данных\".\n\n☑ Используйте кнопки меню для навигации по материалам.\n\n💻 Разработка: @magecode\n📚 Наполнение и документирование: @holera5'

# Команды
commands = [
    types.BotCommand('start', 'Запустить бота'),
    types.BotCommand('topics', 'Открыть темы'),
    types.BotCommand('tasks', 'Открыть задания'),
    types.BotCommand('search', 'Открыть поиск'),
    types.BotCommand('back', 'Возвращает назад')
]

# Клавиатура бота
keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.row(*[BUT_TOPICS, BUT_TASKS])
keyboard_main.row(*[BUT_SEARCH, BUT_FAQ])

keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_back.row(BUT_BACK)