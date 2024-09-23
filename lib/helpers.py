# from models.category import Category
# from models.supplier import Supplier
# from models.inventory import Inventory
# from models.transaction import Transaction
from category_menu import CategoryMenu
from supplier_menu import SupplierMenu
from inventory_menu import InventoryMenu
from transaction_menu import TransactionMenu

from db.base import Base
from db.tools import engine
from datetime import datetime

Base.metadata.create_all(engine)

def add_inventory ():
    name = input('enter inventory name: ')
    quantity = int(input('enter inventory quantity: '))
    unit_price = float(input('enter inventory unit price: '))
    category_id = int(input('enter inventory category'))
    supplier_id = int(input('enter inventory supplier'))
    inventory_menu = InventoryMenu()
    inventory_menu.add_inventory(name, quantity, unit_price, category_id, supplier_id)
    if inventory_menu:
        print(f'{name} added successfully')
    else:
        print(f'error adding {name}')
    inventory_menu.close_session()

def add_inventory_to_category():
    category_id = int(input('enter category id: '))
    id = int(input('enter id: '))
    inventory_menu = InventoryMenu()
    inventory_menu.add_inventory_to_category(category_id, id)
    if inventory_menu:
        print(f'{id} added to category successfully')
    else:
        print(f'error adding {id}')
    inventory_menu.close_session()

def find_inventory_by_id():
    id = int(input('enter inventory id: '))
    inventory_menu = InventoryMenu()
    inventory = inventory_menu.find_inventory_by_id(id)
    if inventory:
        print(inventory)
    else:
        print(f'{id} not found')
def remove_inventory_from_category ():
    category_id = int(input('enter inventory category id'))
    id = int(input('enter category id'))
    inventory_menu = InventoryMenu()
    inventory_menu.remove_inventory_from_category(category_id, id)
    if inventory_menu:
        print(f'{category_id} removed successfully')
    else:
        print(f'error removing {category_id}')
    inventory_menu.close_session()

def update_inventory ():
    id = int(input('enter inventory id: '))
    name = input('enter inventory name: ')
    quantity = int(input('enter inventory quantity: '))
    unit_price = float(input('enter inventory unit price: '))
    category_id = int(input('enter inventory category id:'))
    supplier_id = int(input('enter inventory supplier id: '))
    inventory_menu = InventoryMenu()
    inventory_menu.update_inventory(id, name, quantity, unit_price, category_id, supplier_id)
    if inventory_menu:
        print(f'{name} updated successfully')
    else:
        print(f'error updating {name}')
    inventory_menu.close_session()

def add_category():
    name =input('enter category name: ')
    description = input('enter category description: ')
    category_menu = CategoryMenu()
    category_menu.add_category(name, description)
    if category_menu:
        print(f'{name} added successfully')
    else:
        print(f'error adding {name}')
    category_menu.close_session()

def find_category_by_id():
    id = int(input('Enter category id'))
    category_menu = CategoryMenu()
    category = category_menu.find_category_by_id(id)
    if category:
        print(f'{category.name}, {category.description} found successfully')
    else:
        print(f'{id} not found')
    category_menu.close_session()

def get_all_by_category():
    category_menu = CategoryMenu()
    categories = category_menu.get_all_category()
    print('Categories:')
    for category in categories:
        print(f'ID: {category.id}, Name: {category.name}, Description: {category.description}')
    category_menu.close_session()

def update_category():
    id = int(input('enter category id'))
    name = input('enter category name: ')
    description = input('enter category description: ')
    category_menu = CategoryMenu()
    category_menu.update_category(id, name, description)
    if category_menu:
        print(f'{name} updated successfully')
    else:
        print(f'error updating {name}')
    category_menu.close_session()

def delete_category():
    id = int(input('enter category id'))
    category_menu = CategoryMenu()
    category_menu.delete_category(id)
    if category_menu:
        print(f'{id} deleted successfully')
    else:
        print(f'error deleting {id}')
    category_menu.close_session()

def add_supplier():
    name = input('enter supplier name: ')
    email = input('enter supplier email: ')
    phone = input('enter supplier phone: ')
    address = input('enter supplier address: ')
    supplier_menu = SupplierMenu()
    supplier = supplier_menu.add_supplier(name, email, phone, address)
    if supplier:
        print(f'{name} added successfully')
    else:
        print(f'error adding {name}')
    supplier_menu.close_session()

def find_supplier_by_id():
    id = int(input('enter supplier id'))
    supplier_menu = SupplierMenu()
    supplier_menu.find_supplier_by_id(id)
    if supplier_menu:
        print(f'{id} found successfully')
    else:
        print(f'{id} not found')
    supplier_menu.close_session()

def get_all_suppliers():
    supplier_menu = SupplierMenu()
    suppliers = supplier_menu.get_all_suppliers()
    print('Suppliers:')
    for supplier in suppliers:
        print(f'ID: {supplier.id}, Name: {supplier.name}, Email: {supplier.email}, Phone: {supplier.phone}, Address: {supplier.address}')
    supplier_menu.close_session()

def update_supplier():
    id = int(input('enter supplier id'))
    name = input('enter supplier name: ')
    email = input('enter supplier email: ')
    phone = input('enter supplier phone: ')
    address = input('enter supplier address: ')
    supplier_menu = SupplierMenu()
    supplier_menu.update_supplier(id, name, email, phone, address)
    if supplier_menu:
        print(f'{name} updated successfully')
    else:
        print(f'error updating {name}')
    supplier_menu.close_session()

def delete_supplier():
    id = int(input('enter supplier id'))
    supplier_menu = SupplierMenu()
    supplier_menu.delete_supplier(id)
    if supplier_menu:
        print(f'{id} deleted successfully')
    else:
        print(f'error deleting {id}')
    supplier_menu.close_session()

def add_transaction():
    transaction_type = input('enter transaction type (purchase or sale): ')
    quantity = int(input('enter transaction quantity: '))
    transaction_date_str= input('enter transaction date (YYYY-MM-DD): ')
    inventory_id = int(input('enter inventory id: '))
    try:
        transaction_date = datetime.strptime(transaction_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    transaction_menu = TransactionMenu()
    transaction = transaction_menu.add_transaction(transaction_type, quantity, transaction_date, inventory_id)
    if transaction:
        print(f'{transaction_type} added successfully')
    else:
        print(f'error adding {transaction_type}')
    transaction_menu.close_session()

def add_transaction_to_inventory():
    inventory_id = int(input('enter inventory id: '))
    transaction_id = int(input('enter transaction id: '))
    transaction_menu = TransactionMenu()
    transaction_menu.add_transaction_to_inventory(inventory_id, transaction_id)
    if transaction_menu:
        print(f'{transaction_id} added to inventory successfully')
    else:
        print(f'error adding {transaction_id}')
    transaction_menu.close_session()

def find_transaction_by_id():
    id = int(input('enter transaction id'))
    transaction_menu = TransactionMenu()
    transaction_menu.find_transaction_by_id(id)
    if transaction_menu:
        print(f'{id} found successfully')
    else:
        print(f'{id} not found')
    transaction_menu.close_session()

def remove_transaction_from_inventory():
    inventory_id = int(input('enter inventory id: '))
    transaction_id = int(input('enter transaction id: '))
    transaction_menu = TransactionMenu()
    transaction_menu.remove_transaction_from_inventory(inventory_id, transaction_id)
    if transaction_menu:
        print(f'{transaction_id} removed from inventory successfully')
    else:
        print(f'error removing {transaction_id}')
    transaction_menu.close_session()

def update_transaction():
    id = int(input('enter transaction id'))
    transaction_type = input('enter transaction type (purchase or sale): ')
    quantity = int(input('enter transaction quantity: '))
    transaction_date_str = input('enter transaction date (YYYY-MM-DD): ')
    inventory_id = int(input('enter inventory id: '))
    try:
        transaction_date = datetime.strptime(transaction_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    transaction_menu = TransactionMenu()
    transaction_menu.update_transaction(id, transaction_type, quantity, transaction_date, inventory_id)
    if transaction_menu:
        print(f'{transaction_type} updated successfully')
    else:
        print(f'error updating {transaction_type}')
    transaction_menu.close_session()






