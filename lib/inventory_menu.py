from db.tools import Session
from db.inventory import Inventory

class InventoryMenu:
    def __init__(self):
        self.session = Session()
    def add_inventory(self, name, quantity, unit_price, category_id, supplier_id):
         inventory = Inventory()
         inventory.name = name
         inventory.quantity = quantity
         inventory.unit_price = unit_price
         inventory.category_id = category_id
         inventory.supplier_id = supplier_id

         try:
             self.session.add(inventory)
             self.session.commit()
             print("Inventory added successfully.")
         except Exception as e:
             print(f"Error adding inventory: {e}")

    def add_inventory_to_category(self, category_id, id):
         inventory = self.session.query(Inventory).get(id)
         if inventory:
             try:
                 inventory.category_id = category_id
                 self.session.commit()
                 print("Inventory added to category successfully.")
             except Exception as e:
                 print(f"Error adding inventory to category: {e}")


    def find_inventory_by_id(self, id):
         return self.session.query(Inventory).get(id)
    
    def remove_inventory_from_category(self, category_id, id): 
        inventory = self.session.query(Inventory).filter_by(id=id, category_id=category_id).first()
        if inventory:
             try:
                 self.session.delete(inventory)
                 self.session.commit()
                 print("Inventory removed from category successfully.")
             except Exception as e:
                 print(f"Error removing inventory from category: {e}")

    def update_inventory(self, id, name=None, quantity=None, unit_price=None, category_id=None, supplier_id=None):
       inventory = self.find_inventory_by_id(id)
       if inventory:
           try:
               if name: inventory.name = name
               if quantity: inventory.quantity = quantity
               if unit_price: inventory.unit_price = unit_price
               if category_id: inventory.category_id = category_id
               if supplier_id: inventory.supplier_id = supplier_id
               self.session.commit()
               print("Inventory updated successfully.")
           except Exception as e:
               print(f"Error updating inventory: {e}")
    
    def close_session(self):
        self.session.close()