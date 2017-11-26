import logging
import sys
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler, MessageHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

MIRROR = "Зеркало"
CONTACTS = "Контакты"


def start(bot, update):
    keyboard = [[MIRROR, CONTACTS]]
    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Я бот БК WindBet.\n'
        'Я могу подсказать адрес актуального зеркала и контактные данные.',
        reply_markup=reply_markup)


def messageText(bot, update):
    text = update.message.text

    foo = {
        MIRROR: mirror,
        CONTACTS: contacts
    }

    try:
        bar = foo[text]
    except KeyError as e:
        bar = mirror

    bar(bot, update)


def deleteKeyboard(bot, update):
    update.message.reply_text('deleted', reply_markup=ReplyKeyboardRemove())


def mirror(bot, update):
    update.message.reply_text(
        'Адреса актуальных зеркал:\n'
        'windbet1.com\n'
        'windbet2.com\n'
        'windbet3.com\n'
    )


def contacts(bot, update):
    update.message.reply_text(
        'Техподдержка: tech@windbet.com')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main(token):
    if not token:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))

    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('d', deleteKeyboard))
    dp.add_handler(MessageHandler(Filters.text, messageText))

    # log all errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    token = sys.argv[1]
    main(token)
