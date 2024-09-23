from db.tools import Session
from db.transaction import Transaction


class TransactionMenu:
    def __init__(self):
        self.session = Session()

    def add_transaction(self, transaction_type, quantity, transaction_date, inventory_id):
         transaction = Transaction()
         transaction.transaction_type = transaction_type
         transaction.quantity = quantity
         transaction.transaction_date = transaction_date
         transaction.inventory_id = inventory_id

         try:
             self.session.add(transaction)
             self.session.commit()
             print("Transaction added successfully.")
         except Exception as e:
             print(f"Error adding transaction: {e}")

    def add_transaction_to_inventory(self, inventory_id, id):
         transaction = self.session.query(Transaction).get(id)
         if transaction:
             try:
                 transaction.inventory_id = inventory_id
                 self.session.commit()
                 print("Transaction added to inventory successfully.")
             except Exception as e:
                 print(f"Error adding transaction to inventory: {e}")
    
    def find_transaction_by_id(self, id):
         transaction = self.session.query(Transaction).get(id)
         return transaction     

    def remove_transaction_from_inventory(self, inventory_id, id): 
        transaction = self.session.query(Transaction).filter_by(id=id, inventory_id=inventory_id).first()
        if transaction:
             try:
                 self.session.delete(transaction)
                 self.session.commit()
                 print("Transaction removed from inventory successfully.")
             except Exception as e:
                 print(f"Error removing transaction from inventory: {e}")
 
    def update_transaction(self, id, transaction_type=None, quantity=None, transaction_date=None, inventory_id=None):
       transaction = self.find_transaction_by_id(id)
       if transaction:
           try:
               if transaction_type: transaction.transaction_type = transaction_type
               if quantity: transaction.quantity = quantity
               if transaction_date: transaction.transaction_date = transaction_date
               if inventory_id: transaction.inventory_id = inventory_id
               self.session.commit()
               print("Transaction updated successfully.")
           except Exception as e:
               print(f"Error updating transaction: {e}")
     
    def close_session(self):
        self.session.close()