import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from tg.views import DbHelper
db=DbHelper()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update,context):
    main_button=[
        ['🛒 Buyurtma qilish'],
        [
            '🛍 Buyurtmalarim',
            '👨‍👨‍👧‍👧 EVOS Oilasi'
        ],
        [
            '📝 Fikr bildirish',
            '⚙️Sozlamalar'
        ]
    ]

    user = update.message.from_user
    update.message.reply_html('Assalomu aleykum <b>{}!</b>'.format(user.first_name),
                              reply_markup=ReplyKeyboardMarkup(main_button, resize_keyboard=True,one_time_keyboard=True))

    return 1

def buyurtma(update, context):
    db.category_parent()
    for data in category_parent:
        print("mana datalar", data)
    update.message.reply_html('buyurtmaga keldim')



def buyurtmalarim(update,context):
    update.message.reply_html('buyurtmaga keldim')

def oila(update, context):
    update.message.reply_html('oilaga keldim')

def fikr(update, context):
    update.message.reply_html('fikrga keldim')

def sozlama(update, context):
    update.message.reply_html('fikrga keldim')

def cancel(update,context):
    update.message.reply_html('cancelga keldim')


def help_command(update: Update, _: CallbackContext) -> None:

    update.message.reply_text('Help!')


def echo(update: Update, _: CallbackContext) -> None:

    update.message.reply_text(update.message.text)
