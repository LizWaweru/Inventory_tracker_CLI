# Import the necessary modules from the SQLAlchemy library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine that connects to the SQLite database
engine = create_engine('sqlite:///inventories.db')

#Create a configured "Session" class
Session = sessionmaker(bind=engine)


    