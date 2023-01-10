from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

#taking the token
token = open("token.txt").readline()
updater=Updater(token, use_context=True)

my_list=list()

def start(update, context):
    update.message.reply_text("Ciao! Sono Shopping List Bot, il tuo assistente per la spesa.\n")

def help(update, context):
    update.message.reply_text("Comandi:\n/add per aggiungere un prodotto\n/show per visualizzare la lista\n/check per spuntare un elemento dalla lista\n/delete per svuotere la lista\n")

def unknown(update, context):
    update.message.reply_text("Comando non valido, scrivi /help per conoscere la lista di comandi\n")

def add(update, context):
    x=context.args[0]
    #concatenare in x le varie stringe di args con il +
    if x in my_list:
        update.message.reply_text("Il prodotto è già in lista.\n")
    else:
        my_list.append(x)
    #si deve correggere la lettura di args per elementi formati da più parole

def show(update, context):
    update.message.reply_text('Lista:\n- '+'\n- '.join(my_list))
    #x=1
    #update.message.reply_text(str(x)+'. '+('\n'+str(x)+'. ').join(my_list))

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('add', add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('show', show))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()



