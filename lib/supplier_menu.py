from db.tools import Session
from db.supplier import Supplier

class SupplierMenu:
    def __init__(self):
        self.session = Session()

    def add_supplier(self, name, email, phone, address):
        supplier = Supplier()
        try:
            supplier.name = name
            supplier.email = email
            supplier.phone = phone
            supplier.address = address
            self.session.add(supplier)
            self.session.commit()
            print("Supplier added successfully.")
            return supplier
        except Exception as e:
            self.session.rollback()
            print(f"Error adding supplier: {str(e)}")
            return None
        
    def find_supplier_by_id(self, id):
        supplier = self.session.query(Supplier).get(id)
        return supplier
    
    def get_all_suppliers(self):
        suppliers = self.session.query(Supplier)
        return [supplier for supplier in suppliers]
    
    def update_supplier(self, id, name, email, phone, address):
        supplier = self.find_supplier_by_id(id)
        if supplier:
            try:
                supplier.name = name
                supplier.email = email
                supplier.phone = phone
                supplier.address = address
                self.session.commit()
                print("Supplier updated successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error updating supplier: {str(e)}")

    def delete_supplier(self, id):
        supplier = self.find_supplier_by_id(id)
        if supplier:
            try:
                self.session.delete(supplier)
                self.session.commit()
                print("Supplier deleted successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error deleting supplier: {str(e)}")

    def close_session(self):
        self.session.close()




    
