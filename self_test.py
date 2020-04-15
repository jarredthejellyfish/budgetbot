
class SelfTest:
  def __init__(self, fname='transactions.csv'):
    self.fname = fname

  def database_testing(self):
    try:
      from database_classes import Transaction, Database

      try:
        test_transaction = Transaction('This is a test', 123.321, '04/20/2020', '00:00:00')
        test_transaction_repr = test_transaction.as_dict()

        try:
          test_db = Database(self.fname)
        except:
          print('Database class is not functional')
          raise

        try:
          test_db.in_database(test_transaction)
        except:
          print('.in_database method is not functional.')
          raise

        try:
          test_db.add_transaction(test_transaction)
        except:
          print('.add_transaction method is not functional')
          raise

        try:
          test_db.get_transactions('This is a test', '04/20/2020')
        except:
          print('.get_transaction method is not functional.')
          raise

        try:
          test_db.remove_transaction(test_transaction)
        except:
          print('.remove_transaction method is not functional.')
          raise
       
        print('\n','No major errors were found within the database and transaction classes.', '\n')
        
      except:
        print('Transaction class is not functional')
        raise

    except:
        print('Database classes file contains errors.')

      

    