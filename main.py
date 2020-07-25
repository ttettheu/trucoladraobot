from telegram.ext import Updater

updater = Updater(token='1136019947:AAFHkKqT8clc8FWunqrgW_Tj6GBsWveVl2Y', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Siga esses passos:\
        \n1. Adicione este bot a um grupo\
        \n2. No grupo, inicie um novo jogo com /new ou entre em um jogo já em execução com /join\
        \n3. Após pelo menos dois jogadores entrarem, inicie o jogo com /start \
        \n\
        \nIdioma e outras configurações: /settin Outros comandos (apenas criador do jogo):\
            \n/close - Fechar lobby\
            \n/open - Hall de entrada aberto\
            \n/kill - finaliza o jogo\
            \n/kick - Selecione um jogador para chutar, respondendo a ele\
            \n/enable_translations - Traduza textos relevantes para todos os idiomas falados em um jogo\
            \n/disable_translations - Use inglês para esses textos")
#comando start de inicio
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#repete todas mensagens
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

#adicionar comandos
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text="testcaps")

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

#inline mode
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


#mensagem para comando não reconhecido pelo inline
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)





updater.start_polling()

