from datetime import datetime
import csv

class Transaction:
    def __init__(self, concept, amount, date=None, time=None):
        self.concept = concept
        self.amount = round(amount,2)
        if not time:
            now = datetime.now()
            self.date = now.strftime('%D')
            self.time = now.strftime('%H:%M')
        else:
            self.date = date
            self.time = time

    def as_list(self):
        return [str(self.date+ self.time+ self.amount+ self.concept + '\r\n')]

    def __repr__(self):
        if self.amount > 0:
            return 'Got {} from {} on {} at {}'.format(self.amount, self.concept, self.date, self.time)
        else:
            return 'Spent {} at {} on {} at {}'.format(self.amount, self.concept, self.date, self.time)

class Database:
    def __init__(self, filename):
        self.filename = filename
    
    def add_transaction(self, transaction):
        if self.in_database(transaction):
            print('no')

    def in_database(self, transaction):
        with open(self.filename, 'r', newline='') as file:
            transactions = [transaction for transaction in file][1:]
        print(transactions[0])
        print(transaction.as_list())

starbucks = Transaction('Starbucks', -123.32, '4/20/20', '4:20')
print(starbucks)
db = Database('transactions.csv')
db.add_transaction(starbucks)