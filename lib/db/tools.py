# Import the necessary modules from the SQLAlchemy library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///inventories.db')
Session = sessionmaker(bind=engine)


    