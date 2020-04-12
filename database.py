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
        return self.date + ',' + self.time + ',' + str(self.amount) + ',' + self.concept + '\r\n'

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
            raise FileExistsError
        else:
            with open(self.filename, 'a') as file:
                writer = csv.writer(file)
                writer.writerow([transaction.date, transaction.time, transaction.amount, transaction.concept])
                print('written')

    def in_database(self, transaction):
        with open(self.filename, 'r', newline='') as file:
            transactions = [transaction for transaction in file][1:]
            for transaction_ffile in transactions:
                if transaction_ffile == transaction.as_list():
                    return True
            return None        