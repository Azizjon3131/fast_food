from django.core.management.base import BaseCommand, CommandError

from ._actions import start,cancel,echo,buyurtmalarim,oila,fikr,sozlama,buyurtma,inline_menu,qabul, location,contact
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
                          MessageHandler(Filters.regex('π Buyurtma qilish'), buyurtma),
                          ],
            states={
                1: [
                    MessageHandler(Filters.regex('π Buyurtma qilish'), buyurtma),
                    MessageHandler(Filters.regex('π Buyurtmalarim'), buyurtmalarim),
                    MessageHandler(Filters.regex('π¨βπ¨βπ§βπ§ EVOS Oilasi'), oila),
                    MessageHandler(Filters.regex('π Fikr bildirish'), fikr),
                    MessageHandler(Filters.regex('β Sozlamalar'), sozlama),
                ],
                2:[
                    CallbackQueryHandler(inline_menu),
                    MessageHandler(Filters.regex('^(π Buyurtma qilish)$'), buyurtma)
                ],
                3:[
                    MessageHandler(Filters.location,location),
                    MessageHandler(Filters.contact,contact),
                    MessageHandler(Filters.regex('β¬οΈOrtga'),start),
                ],

            },
            fallbacks=[CommandHandler('cancel', cancel)]
        )

        dispatcher.add_handler(covn_handler)
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start))

        updater.start_polling()

        updater.idle()

        self.stdout.write(self.style.SUCCESS('Shu yer Ishladi'))