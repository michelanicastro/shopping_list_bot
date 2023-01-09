from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

#taking the token
token = open("token.txt").readline()

updater=Updater(token, use_context=True)

def start(update, context):
    update.message.reply_text("Ciao! Sono Shopping List Bot, il tuo assistente per la spesa.\n")

def help(update, context):
    update.message.reply_text("Comandi:\n/add per aggiungere un prodotto\n/list per visualizzare la lista\n/check per spuntare un elemento dalla lista\n/delete per svuotere la lista\n")

def unknown(update, context):
    update.message.reply_text("Comando non valido, scrivi /help per conoscere la lista di comandi\n")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()