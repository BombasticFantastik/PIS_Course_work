from sqlalchemy import create_engine,Column,Integer,String,Float,Date
import psycopg2
import abc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


engine=create_engine('postgresql+psycopg2://postgres:12345@localhost/pis_base')
engine.connect()
Base=declarative_base()
class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    seller_id=Column(Integer)
    name=Column(String)
    article=Column(Integer)
    price=Column(Float)
    count=Column(Integer)
    
class Seller(Base):
    __tablename__='sellers'
    id=Column(Integer,primary_key=True)
    login=Column(String)
    password_hash=Column(String)
    INN=Column(Integer)
    legal_entity=Column(String)
    address=Column(String)
    registred_in=Column(Date)

class Admin(Base):
    __tablename__='admins'
    id=Column(Integer,primary_key=True)
    login=Column(String)
    password_hash=Column(String)
    INN=Column(Integer)
    legal_entity=Column(String)
    address=Column(String)
    registred_in=Column(Date)

class Order(Base):
    __tablename__='orders'
    id=Column(Integer,primary_key=True)
    seller_id=Column(Integer)
    admin_id=Column(Integer)
    created_in=Column(Date)
    status=Column(String)
    total_price=Column(Float)
    
class Order_Item(Base):
    __tablename__='order_items'
    item_id=Column(Integer,primary_key=True)
    order_id=Column(Integer,primary_key=True)
    count=Column(Integer)

    
    