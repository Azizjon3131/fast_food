from django.core.management.base import BaseCommand, CommandError

from ._actions import start,cancel,echo,buyurtmalarim,oila,fikr,sozlama,buyurtma,inline_menu,qabul
from django.conf import settings
import logging

from telegram import Update, ForceReply
from telegram.ext import (Updater, CommandHandler,
    MessageHandler, Filters, CallbackContext,
    ConversationHandler,CallbackQueryHandler)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(settings.BOT_TOKEN)

        dispatcher = updater.dispatcher

        covn_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start),
                          MessageHandler(Filters.regex('🛒 Buyurtma qilish'), buyurtma),
                          ],
            states={
                1: [
                    MessageHandler(Filters.regex('🛒 Buyurtma qilish'), buyurtma),
                    MessageHandler(Filters.regex('🛍 Buyurtmalarim'), buyurtmalarim),
                    MessageHandler(Filters.regex('👨‍👨‍👧‍👧 EVOS Oilasi'), oila),
                    MessageHandler(Filters.regex('📝 Fikr bildirish'), fikr),
                    MessageHandler(Filters.regex('⚙ Sozlamalar'), sozlama),
                ],
                2:[
                    CallbackQueryHandler(inline_menu),
                    MessageHandler(Filters.regex('^(🛒 Buyurtma qilish)$'), buyurtma)
                ],
                3:[
                    MessageHandler(Filters.regex('📍 Geo locatsiya yuborish'),qabul),
                    MessageHandler(Filters.regex('⬅️Ortga'),start),
                ],

            },
            fallbacks=[CommandHandler('cancel', cancel)]
        )

        dispatcher.add_handler(covn_handler)
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start))

        updater.start_polling()

        updater.idle()

        self.stdout.write(self.style.SUCCESS('Shu yer Ishladi'))