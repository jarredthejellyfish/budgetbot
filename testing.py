import random
import re
from database_classes import Transaction, Database
greetings = (
        'Hey there fellow finance enthusiast! I\'m @BudgetBot.',
        'Hi human, I\'m @BudgetBot'
    )


def get_transaction():
    stringy = input('Gimme a string:\n').lower()
    stringy = re.sub(r'[^\w]', ' ', stringy)
    stringy = re.sub(r'\s+', ' ', stringy)
    return stringy

class Bot:
    def __init__(self):
        self.regex_dict = {'spent':r'.*spent\s*(?:\w\s+)?(\d+)(?:\s+(?:at|on)\s+(\w+))?.*',
                           'gave':r'.*?gave.((\w+).(\d+)).*',
                           'received':r'.*received\s*(\d+)\s*(?:\w+\s*)?from\s*(\w+).*'
                        }

        self.db = Database()

    def match_intent(self, context):
        for intent, regex in self.regex_dict.items():
            match = re.match(regex, stringy)

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

bot = Bot()
'''
while True:
    stringy = get_transaction()
    if bot.match_intent(stringy):
        pass
    else:
        print('Couldn\'t be added to DB')
        break'''
