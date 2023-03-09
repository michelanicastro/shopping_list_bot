from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

#taking the token
token = open("token.txt").readline()
updater=Updater(token, use_context=True)

my_list=list()

def start(update, context):
    update.message.reply_text("Ciao! Sono Shopping List Bot, il tuo assistente per la spesa\n")

def help(update, context):
    update.message.reply_text("Comandi:\n/add articolo  ->  inserisce l'articolo\n/remove articolo  ->  elimina l'articolo\n/show  ->  mostra la lista\n/delete  ->  svuota la lista\n")

def unknown(update, context):
    update.message.reply_text("Comando non valido, scrivi /help per conoscere la lista di comandi\n")

def add(update, context):
    x=""
    for y in context.args:
        x+=(y+" ")

    if x=="":
        update.message.reply_text("Comando non valido.\nScrivi '/add nome_articolo' per aggiungere un prodotto alla lista")
        return
    
    if x in my_list:
        update.message.reply_text("Il prodotto è già in lista\n")
    else:
        my_list.append(x)
        update.message.reply_text(x+" aggiunto alla lista\n")

def remove(update, context):
    x=""
    for y in context.args:
        x+=(y+" ")

    if x=="":
        update.message.reply_text("Comando non valido.\nScrivi '/remove nome_articolo' per eliminare un prodotto dalla lista")
        return

    if x in my_list:
        my_list.remove(x)
        update.message.reply_text(x+" rimosso dalla lista\n")
    else:
        update.message.reply_text("Il prodotto non è in lista\n")

def delete(update, context):
    my_list.clear()
    update.message.reply_text("La lista è stata svuotata\n")

def show(update, context):
    if not my_list:
        update.message.reply_text("La lista è vuota\n")
    else:
        update.message.reply_text('Lista:\n- '+'\n- '.join(my_list))

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('add', add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('remove', remove, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('delete', delete))
updater.dispatcher.add_handler(CommandHandler('show', show))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()



