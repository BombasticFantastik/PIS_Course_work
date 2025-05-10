from sqlalchemy import create_engine
import psycopg2
import abc
from classes import Item
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from AlchFacade import AlchFacade
import yaml


option_path='config.yaml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)


engine=create_engine(option['path'])
engine.connect()
#Base=declarative_base()

Session=sessionmaker(bind=engine)
session=Session()

#


Fasade=AlchFacade(engine,session)
#Fasade.delete(item0)
a=Fasade.get_items(id=1)
Fasade.delete(a[0])
Fasade.save()
#Fasade.add()