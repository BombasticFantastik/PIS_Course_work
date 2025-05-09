from sqlalchemy import create_engine,Column,Integer,String,Float,Date
import psycopg2
import abc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from Model.AlchFacade import 
from bd_classes import Item

engine=create_engine()
engine.connect()

Base=declarative_base()

Session=sessionmaker(bind=engine)
sesion=Session()

fac=AlchFacade(engine=engine,session=sesion)