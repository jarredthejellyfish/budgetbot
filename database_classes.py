from datetime import datetime
import csv

class Transaction:
    # Initialize transaction and add values to self.
    def __init__(self, amount, concept='Not stated', date=None, time=None):
        self.concept = concept
        self.amount = round(amount,2)
        if not time:
            now = datetime.now()
            self.date = now.strftime('%D')
            self.time = now.strftime('%H:%M')
        else:
            self.date = date
            self.time = time

    # Return all values from transaction as a dictionarty object.
    def as_dict(self):
        return {'DATE': self.date, 'TIME': self.time, 'AMOUNT': str(self.amount), 'CONCEPT': self.concept}
    
    # Representation method
    def __repr__(self):
        # If the transaction adds to balance.
        if self.amount > 0:
            return 'Got {} from {} on {} at {}'.format(self.amount, self.concept, self.date, self.time)
        # If the transaction removes from balance.    
        else:
            return 'Spent {} at {} on {} at {}'.format(self.amount, self.concept, self.date, self.time)

class Database:
    def __init__(self, chat_id):
        # Generate the filename for the database file.
        fname = './userdata/' + str(chat_id) + '.csv'

        try:
            f = open(fname)
            print('opened')
        except:
            f = open(fname, 'w+')
            writer = csv.writer(f)
            writer.writerow(['DATE', 'TIME', 'AMOUNT', 'CONCEPT'])
        
        f.close
        self.filename = fname
    
    # Add transaction as row to the file @ self.filename
    def add_transaction(self, transaction):
        # Check if transaction has already been added.
        if self.in_database(transaction):
            raise FileExistsError
        # If it has not, add it.
        else:
            # Open CSV file.
            with open(self.filename, 'a') as file:
                writer = csv.writer(file)
                # Write transaction details to last row.
                writer.writerow([transaction.date, transaction.time, transaction.amount, transaction.concept])

    # Check if transaction item is in database.
    def in_database(self, transaction):
        # Open csv file as list of OrederedDict objects.
        db_file = csv.DictReader(open(self.filename))
        # Iterate through OrederedDicts 
        for row in db_file:
            # Compare with the .as_dict() method from Transaction().
            if dict(row) == transaction.as_dict():
                return True
        # If no matches exist return None.
        return None

    # Get all transactions that match a certain criteria.
    def get_transactions(self, concept, date):
        #Initialize empty list for transactions in CSV.
        matched_transactions = []
        # Initialize DictReader.
        reader = csv.DictReader(open(self.filename))
        # Iterate through reader.
        for row in reader:
            # If criteria match with any values in rows.
            if row.get('CONCEPT') == concept and row.get('DATE') == date:
                # Add that dictionary to the empty list.
                matched_transactions.append(row)
        # If there are items in matched_transactions, return the list.
        if len(matched_transactions) > 0:
            return matched_transactions
        else:
            return None

    def remove_transaction(self, transaction):
        # Storage for non-removed transactions.
        transaction_list = []
        # CSV headers
        headers = ['DATE', 'TIME', 'AMOUNT', 'CONCEPT']
        # Open CSV file into a dictionary reader.
        reader = csv.DictReader(open(self.filename, 'r'))
        for row in reader:
            # If the read dictionary from the current row does not match the 
            # transaction, store itin the transaction_list.
            if not transaction.as_dict() == dict(row):
                transaction_list.append(dict(row))
        # Delete all contents from file
        open(self.filename, 'w').close()
        # Open the blank CSV as into a file object.
        with open(self.filename, 'a') as file:
                # Create a CSV writer with file object as input.
                writer = csv.writer(file)
                # Write header to file.
                writer.writerow(['DATE', 'TIME', 'AMOUNT', 'CONCEPT'])
                # Write each row stored in transaction_list to the CSV file.
                for row in transaction_list:
                    writer.writerow(row.values())