from database_classes import Transaction, Database
from self_test import SelfTest
from sensitive_data import token

import telegram
from telegram.ext import CallbackQueryHandler, CommandHandler, Filters, MessageHandler, Updater, dispatcher, run_async
from telegram import update

import random
import re

greetings = (
        'Hey there fellow finance enthusiast! I\'m @BudgetBot.',
        'Hi human, I\'m @BudgetBot.',
        'Heyo, get ready to finance! I\'m @BudgetBot.'
        )

bot_instances = {}

class BudgetBot:
    def __init__(self, chat_id):
        self.chat_id = chat_id

        self.regex_dict = {'spent':r'.*spent\s*(?:\w\s+)?(\d+)(?:\s+(?:at|on)\s+(\w+))?.*',
                           'gave':r'.*?gave.((\w+).(\d+)).*',
                           'received':r'.*(?:received|got)\s*(\d+)\s*(?:\w+\s*)?from\s*(\w+).*'
                        }

        self.db = Database(chat_id)

    def match_intent(self, message):
        for intent, regex in self.regex_dict.items():
            match = re.match(regex, message)

            if match and intent == 'spent':
                return self.transaction_handler(match.group(2), match.group(1))   

            if match and intent == 'gave':
                return self.transaction_handler(match.group(2), match.group(3))   

            if match and intent == 'received':
                return self.transaction_handler(match.group(2), match.group(1), True)     
        return None
    
    def transaction_handler(self, concept, amount, sign=False):
        if sign is False:
            try:
                amount = abs(int(amount))*-1
                new_transaction = Transaction(amount, concept)
                self.db.add_transaction(new_transaction)
                return True

            except FileExistsError:
                return False
            
            else:
                return None
            
        elif sign is True:
            try:
                amount = abs(int(amount))
                new_transaction = Transaction(amount, concept)
                self.db.add_transaction(new_transaction)
                return True

            except FileExistsError:
                return False
            
            else:
                return None

    def text_formatter(self, message):
        message = re.sub(r'[^\w]', ' ', message)
        message = re.sub(r'\s+', ' ', message)
        return message.lower()


updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    response = random.choice(greetings) + '\nI will help you manage your spending and get whatever you send me into a spreadhseet.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    print(bot_instances)


@run_async
def bot_handler(update, context):
    chat_id = update.effective_chat.id   
    if chat_id not in bot_instances.keys():
        bot = BudgetBot(chat_id)
        bot_instances[chat_id] = bot
    else:
        bot = bot_instances[chat_id]
    
    message = bot.text_formatter(update.message.text)

    if bot.match_intent(message) == True:
        context.bot.send_message(chat_id=bot.chat_id, text='Successfully added to DB')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

plain_text_handler = MessageHandler(Filters.text, bot_handler)
dispatcher.add_handler(plain_text_handler)

updater.start_polling()