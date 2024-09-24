# Inventory Management CLI System
The Inventory Management System is a comprehensive application designed to manage products, suppliers, categories, inventories, and transactions. This system is built using Python and SQLAlchemy, providing CRUD operations for users keep track of stock levels. It allows business manage supplier information, and monitor transaction histories, providing a robust solution for inventory management.

## Models and relationships

The models represent real-world entities: Inventory, Category, Supplier and Transaction.

- Inventory-Transaction:One-to-many relationship. An inventory can have multiple transactions but a transaction is related to one inventory item.
- Category: One category can have many inventories.
- Supplier: One-to-many;A supplier can supply many inventories.
  Here a representation of the ERD relations: https://dbdiagram.io/d/Inventory_ERD-66f054a3a0828f8aa6a9bc54

## Features

- Add, update, and delete categories and suppliers
- Manage inventory items with detailed information
- Track transactions (stock in/out) for inventory items
- Search and filter functionalities for inventory and supplier records.

### Installation and set up

- Ensure you have installed Python 3.7 or higher

- Clone the repository:

```bash
   git clone https://git@github.com:crea-tivecoder/Inventory_tracker_CLI.git
   cd Inventory_tracker_CLI
```

- Create a virtual environment

```bash
python -m venv venv
```

- Install the required packages

```bash
pip install sqlalchemy
```

- Generating Pipenv
  Install any dependencies you'll need for your project, like SQLAlchemy and Alembic

```bash
pipenv install sqlalchemy alembic
```

### Generating Your Database

Once you're in your environment, you can start development.
Setting up your database.
`cd` into the `lib/db` directory, then run `alembic init migrations` to set up Alembic.
Modify line 63 in `alembic.ini` to point to the database you intend to create, then replace line 26 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

Navigate to `lib/db` and start creating the models.
Regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
`alembic upgrade head` to track your modifications to the database and create checkpoints in case of any need to roll the modifications back.

Run `cli.py` script to generate some test data.

### Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`.

`print()` statements in the CLI script let the
user know the input message they would want to choose from.

### Usage menu

Run `python cli.py` to run the application via the CLI
The main menu allows the user to:

1.  Inventory menu

    1.1 add inventory: Adds a new inventory item.
    1.2 add Inventory to category: Associates an inventory with a category.
    1.3 find inventory by id: Finds an inventory item by its ID.
    1.4 update inventory: Modify the details of an existing inventory item
    1.5 remove Inventory from category: Deletes an inventory from a category.

2.  Category menu
    2.1 add category: Adds a new product category.
    2.2 Update category: Modify a category's name or description
    2.3 find category by id: Finds and displays a category by ID
    2.4 Delete category: Removes a category from the system

3.  Transaction menu
    4.0 add transaction: Adds a new transaction (either stock-in or stock-out).
    4.1 add transaction to Inventory: Associate a transaction with an inventory item.
    4.2 remove transaction from inventory: Detach a transaction from an inventory item.
    4.3 Get all transactions that belong to an inventory
    4.4 update transaction: Modify transaction details.
    4.5 find transaction by id: Retrieves transaction details by ID.

4.  Supplier menu
    5.0 find supplier by id: Retrieves a supplier's details using its ID.
    5.0 add supplier: Registers a new supplier.
    5.1 get all supplier/stock/category: Lists all suppliers.
    6.2 update supplier/stock/category: Updates suppliers and quantity
    6.3 delete supplier/stock/category: Deletes supplier
