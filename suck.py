
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    phone_number = user['phone_number']

    if phone_number:
        update.message.reply_text('Вы уже прошли верификацию и можете получить доступ к каналу.')
    else:
        update.message.reply_text('Чтобы получить доступ к каналу, необходимо пройти верификацию по номеру телефона. Напиши свой номер телефона в формате "+79123456789".')

# Обработчик сообщений
def verify_phone_number(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    phone_number = update.message.text

    # Здесь можно добавить логику отправки кода верификации на указанный номер телефона

    user['phone_number'] = phone_number

    update.message.reply_text('Введите код верификации, который был отправлен на ваш номер телефона.')

def verify_code(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    code = update.message.text
    phone_number = user['phone_number']

    # Здесь можно добавить логику проверки кода верификации

    update.message.reply_text('Верификация прошла успешно! ссылка на канал: [https://t.me/+PLeFCPVQdJZlNTg0]')

def main() -> None:
    # Создаем экземпляр Updater и передаем токен вашего бота
    updater = Updater("6633411988:AAHFW8LWKeZbe6SFYjJczCVnJPRZ5aNG_aU")

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик сообщений для верификации номера телефона
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^\+\d{11}$'), verify_phone_number))

    # Регистрируем обработчик сообщений для проверки кода верификации
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^\d{4}$'), verify_code))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if name == 'main':
    main()