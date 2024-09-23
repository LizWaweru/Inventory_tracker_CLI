from helpers import (
    add_inventory,
    add_inventory_to_category,
    find_inventory_by_id,
    remove_inventory_from_category,
    update_inventory,
    add_category,
    find_category_by_id,
    get_all_by_category,
    update_category,
    delete_category,
    add_supplier,
    find_supplier_by_id,
    get_all_suppliers,
    update_supplier,
    delete_supplier,
    add_transaction,
    find_transaction_by_id,
    remove_transaction_from_inventory,
    add_transaction_to_inventory
)

def main_menu():
    while True:
        print('\nChoose an option:')
        print('1. Add inventory')
        print('2. Add inventory to category')
        print('3. Find inventory by id')
        print('4. Remove inventory from category')
        print('5. Update inventory')
        print('6. Add category')
        print('7. Find category by id')
        print('8. Get all categories')
        print('9. Update category')
        print('10. Delete category')
        print('11. Add supplier')
        print('12. Find supplier by id')
        print('13. Get all suppliers')
        print('14. Update supplier')
        print('15. Delete supplier')
        print('16. Add transaction')
        print('17. Find transaction by id')
        print('18. Remove transaction from inventory')
        print('19. Add transaction to inventory')
        print('20. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            add_inventory()
        elif choice == '2':
            add_inventory_to_category()
            # add_transaction_to_inventory()
        elif choice == '3':
            find_inventory_by_id()
        elif choice == '4':
            remove_inventory_from_category()
        elif choice == '5':
            update_inventory()
        elif choice == '6':
            add_category()
        elif choice == '7':
            find_category_by_id()
        elif choice == '8':
            get_all_by_category()
        elif choice == '9':
            update_category()
        elif choice == '10':
            delete_category()
        elif choice == '11':
            add_supplier()
        elif choice == '12':
            find_supplier_by_id()
        elif choice == '13':
            get_all_suppliers()
        elif choice == '14':
            update_supplier()
        elif choice == '15':
            delete_supplier()
        elif choice == '16':
            add_transaction()
        elif choice == '17':
            find_transaction_by_id()
        elif choice == '18':
            remove_transaction_from_inventory()
        elif choice == '19':
            add_transaction_to_inventory()
        elif choice == '20':
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main_menu()