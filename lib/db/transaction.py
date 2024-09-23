from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from .base import Base

class Transaction(Base):
   __tablename__ = 'transactions'
   id = Column(Integer, primary_key=True)
   transaction_type = Column(String, nullable=False)  # 'in' for stock in, 'out' for stock out
   quantity = Column(Integer, nullable=False)
   transaction_date = Column(DateTime, server_default=func.now())  
   inventory_id = Column(Integer, ForeignKey("inventories.id"))  
   
   def __repr__(self):
      return f'<Inventory(id={self.id}, transaction type={self.transaction_type})>'