from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update

#taking the token
token = 'example'
updater = Updater(token, use_context=True)

shopping_lists = {}

def start(update, context):
    update.message.reply_text("Ciao! Sono Shopping List Bot, il tuo assistente per la spesa.\nScrivi /help per conoscere la lista dei comandi\n")

def help(update, context):
    update.message.reply_text("Comandi:\n/add prodotto  ->  inserisce il prodotto\n/remove prodotto  ->  elimina il prodotto\n/show  ->  mostra la lista\n/clear  ->  svuota la lista\n")

def unknown(update, context):
    update.message.reply_text("Comando non valido, scrivi /help per conoscere la lista dei comandi\n")

def new_user(chat_id):
    if chat_id not in shopping_lists:
        shopping_lists[chat_id]=[]

def add(update, context):
    
    chat_id = update.message.chat_id 
    new_user(chat_id)

    x=""
    for y in context.args:
        x+=(y.lower()+" ")
    if x=="":
        update.message.reply_text("Comando non valido.\nScrivi '/add prodotto' per aggiungere un prodotto alla lista\n")
        return

    if x in shopping_lists[chat_id]:
        update.message.reply_text("Il prodotto è già in lista\n")
    else:
        shopping_lists[chat_id].append(x)
        update.message.reply_text(x+" aggiunto alla lista\n")

def remove(update, context):

    chat_id = update.message.chat_id 
    new_user(chat_id)

    x=""
    for y in context.args:
        x+=(y.lower()+" ")

    if x=="":
        update.message.reply_text("Comando non valido.\nScrivi '/remove prodotto' per eliminare un prodotto dalla lista\n")
        return

    if x in shopping_lists[chat_id]:
        shopping_lists[chat_id].remove(x)  
        update.message.reply_text(x+" rimosso dalla lista\n")
    else:
        update.message.reply_text("Il prodotto non è in lista\n")

def clear(update, context):

    chat_id = update.message.chat_id 
    new_user(chat_id)

    shopping_lists[chat_id].clear()
    update.message.reply_text("La lista è stata svuotata\n")

def show(update, context):

    chat_id = update.message.chat_id 
    new_user(chat_id)

    if shopping_lists[chat_id] == []:
        update.message.reply_text("La lista è vuota\n")
    else:
        update.message.reply_text('Lista:\n- '+'\n- '.join(shopping_lists[chat_id]))

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('add', add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('remove', remove, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('clear', clear))
updater.dispatcher.add_handler(CommandHandler('show', show))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
