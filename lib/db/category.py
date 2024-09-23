from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from .base import Base


class Category(Base):
    __tablename__ = 'products'
    
    #attributes and columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)

    #one to many relationship with suppliers; Inventory: points to a list of suppliers for a product
    #back_populates: automatically creates a backref on the Supplier class to the Product class
    #suppliers: plural attribute because alembic naming when we run migrations

    inventories = relationship('Inventory', backref = backref('category'))
    
