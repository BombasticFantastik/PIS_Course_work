from sqlalchemy import create_engine,Column,Integer,String,Float,Date,BigInteger
#import psycopg2
#import abc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import yaml



option_path='/home/artemybombastic/Рабочий стол/Курсовая работа: проектирование информационных систем/Code/config.yaml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)


engine=create_engine(option['path'])
engine.connect()
Base=declarative_base()


class Item(Base):
    __tablename__='items'
    
    id=Column(Integer,autoincrement=True,primary_key=True)
    seller_id=Column(Integer)
    name=Column(String)
    article=Column(Integer)
    price=Column(Float)
    count=Column(Integer)
    
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    status=Column(String)
    login=Column(String)
    password=Column(String)
    INN=Column(BigInteger)
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
    id=Column(Integer,autoincrement=True,primary_key=True)
    item_id=Column(Integer)
    order_id=Column(Integer)
    count=Column(Integer)

Base.metadata.create_all(engine)   